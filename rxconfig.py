import reflex as rx

config = rx.Config(
    app_name="ai_ats_scanner",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)