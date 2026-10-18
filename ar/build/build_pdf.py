"""Render the proposal PDF from the HTML that build_html.py wrote.

Run after build_html.py:
    python3 ar/build/build_pdf.py

Needs: pip install playwright && python3 -m playwright install chromium
Reads  ar/build/InkZero_AR_Proposal.html
Writes ar/InkZero_AR_Proposal_v3_2026-10-18.pdf (the committed copy)
"""
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
AR = HERE.parent
HTML = HERE / "InkZero_AR_Proposal.html"
PDF = AR / "InkZero_AR_Proposal_v3_2026-10-18.pdf"

FOOTER = (
    '<div style="width:100%;text-align:center;font-family:Helvetica,Arial,sans-serif;'
    'font-size:9px;color:#444;"><span class="pageNumber"></span> of '
    '<span class="totalPages"></span></div>'
)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(HTML.resolve().as_uri())
    page.wait_for_timeout(400)
    page.pdf(
        path=str(PDF),
        format="Letter",
        print_background=True,
        margin={"top": "0.9in", "bottom": "0.9in", "left": "0.9in", "right": "0.9in"},
        display_header_footer=True,
        header_template="<div></div>",
        footer_template=FOOTER,
    )
    browser.close()
print("pdf ok:", PDF)
