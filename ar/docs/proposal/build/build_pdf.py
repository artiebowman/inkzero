"""Render the proposal PDF from the HTML that build_html.py wrote.

Run after build_html.py, on the Mac (it has Helvetica; Linux falls back to Liberation Sans):
    python3 ar/docs/proposal/build/build_pdf.py

Needs: pip install playwright && python3 -m playwright install chromium
Reads  ar/docs/proposal/build/InkZero_AR_Proposal.html
Writes ar/docs/proposal/InkZero_AR_Proposal_v3_2026-10-18.pdf (the committed copy)
"""
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent          # ar/docs/proposal/build
PROPOSAL = HERE.parent                           # ar/docs/proposal
HTML = HERE / "InkZero_AR_Proposal.html"
PDF = PROPOSAL / "InkZero_AR_Proposal_v3_2026-10-18.pdf"

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
