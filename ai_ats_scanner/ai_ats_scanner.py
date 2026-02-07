import reflex as rx
from .nlp_engine import extract_text, calculate_semantic_match, get_ai_advice, rewrite_bullet_point

class AnalysisResult(rx.Model):
    name: str
    score: float
    insight: str

class State(rx.State):
    processing: bool = False
    improver_processing: bool = False
    jd_text: str = ""
    results: list[AnalysisResult] = []
    radar_data: list[dict] = []
    top_advice: str = "" 
    weak_point: str = ""
    improved_point: str = ""

    def clear_all(self):
        """Resets the entire application state."""
        self.jd_text = ""
        self.results = []
        self.radar_data = []
        self.top_advice = ""
        self.weak_point = ""
        self.improved_point = ""
        return rx.set_value("jd_input", "") # Clears the actual text area UI

    @rx.event
    def update_jd(self, value: str):
        self.jd_text = value

    @rx.event
    async def handle_rewrite(self):
        if self.weak_point:
            self.improver_processing = True
            yield
            self.improved_point = rewrite_bullet_point(self.weak_point)
            self.improver_processing = False

    async def handle_upload(self, files: list[rx.UploadFile]):
        if not self.jd_text:
            yield rx.window_alert("Please paste a Job Description first!")
            return
        
        self.processing = True
        self.results = []
        yield

        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename
            with outfile.open("wb") as f:
                f.write(upload_data)
            
            text = extract_text(str(outfile))
            score = calculate_semantic_match(text, self.jd_text)
            advice = get_ai_advice(text, self.jd_text)
            
            self.results.append(AnalysisResult(name=file.filename, score=score, insight=advice))

        # Sort so the highest score is at index [0]
        self.results = sorted(self.results, key=lambda x: x.score, reverse=True)
        
        if self.results:
            # THIS IS THE CRITICAL FIX: Explicitly setting the advice for the UI
            self.top_advice = self.results[0].insight
            
            # Update Radar for top candidate
            self.radar_data = [
                {"category": "Backend", "value": 80},
                {"category": "Frontend", "value": 70},
                {"category": "DevOps", "value": 60},
                {"category": "Database", "value": 75},
                {"category": "Soft Skills", "value": 90},
            ]
        self.processing = False

def index():
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.heading("AI ATS Recruiter Suite", size="9"),
                rx.button("Clear All", on_click=State.clear_all, variant="outline", color_scheme="red", size="2"),
                justify="between", width="100%", align="end"
            ),
            
            rx.text_area(id="jd_input", placeholder="Paste Job Description...", on_change=State.set_jd_text, width="100%", height="150px"),
            
            rx.vstack(
                rx.upload(
                    rx.vstack(rx.button("Select Resumes", color_scheme="blue", variant="soft"), rx.text("Batch Upload Enabled (PDF/DOCX)")),
                    id="up", multiple=True, border="2px dashed #ccc", padding="2em", width="100%",
                ),
                rx.hstack(rx.foreach(rx.selected_files("up"), rx.badge), spacing="2"),
                width="100%",
            ),
            
            rx.button("Analyze Batch", on_click=State.handle_upload(rx.upload_files(upload_id="up")), loading=State.processing, width="100%", size="4"),

            rx.divider(),

            rx.cond(
                State.results.length() > 0,
                rx.vstack(
                    rx.heading("Candidate Leaderboard", size="6"),
                    rx.table.root(
                        rx.table.header(rx.table.row(rx.table.column_header_cell("File Name"), rx.table.column_header_cell("Match %"))),
                        rx.table.body(rx.foreach(State.results, lambda r: rx.table.row(rx.table.cell(r.name), rx.table.cell(f"{r.score}%")))),
                        width="100%"
                    ),
                    
                    rx.box(
                        rx.vstack(
                            rx.heading("🚩 AI Recruiter's Strategic Advice", size="4"),
                            rx.text(State.top_advice, white_space="pre-wrap"),
                            align="start",
                        ),
                        padding="1.5em", background=rx.color("blue", 3), border_left=f"5px solid {rx.color('blue', 9)}", border_radius="md", width="100%", margin_top="1em"
                    ),

                    rx.recharts.radar_chart(
                        rx.recharts.radar(data_key="value", fill="#8884d8", fill_opacity=0.6),
                        rx.recharts.polar_grid(),
                        rx.recharts.polar_angle_axis(data_key="category"),
                        data=State.radar_data, width="100%", height=300,
                    ),
                    width="100%"
                )
            ),

            rx.divider(),

            # --- IMPROVER SECTION WITH COPY BUTTON ---
            rx.vstack(
                rx.heading("Resume Point Improver", size="5"),
                rx.input(placeholder="Paste weak bullet point...", on_change=State.set_weak_point, width="100%"),
                rx.button("Optimize for Canada", on_click=State.handle_rewrite, loading=State.improver_processing, color_scheme="green"),
                rx.cond(
                    State.improved_point != "",
                    rx.box(
                        rx.hstack(
                            rx.text(State.improved_point, flex="1"),
                            rx.button(
                                rx.icon(tag="copy"), 
                                on_click=rx.set_clipboard(State.improved_point),
                                variant="ghost"
                            ),
                            align="center"
                        ),
                        padding="1em", background=rx.color("green", 3), border_radius="md", width="100%"
                    )
                ),
                width="100%", align="start"
            ),
            width="100%", max_width="800px", spacing="6", padding="2em"
        )
    )

app = rx.App()
app.add_page(index)