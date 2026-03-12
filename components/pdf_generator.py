import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

def generate_pdf(scenes: list, title: str = "My AI Story") -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'StoryTitle',
        parent=styles['Title'],
        fontSize=28,
        textColor=colors.HexColor('#ff6b6b'),
        spaceAfter=20
    )
    
    scene_title_style = ParagraphStyle(
        'SceneTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#ff6b6b'),
        spaceBefore=20,
        spaceAfter=10
    )
    
    scene_number_style = ParagraphStyle(
        'SceneNumber',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#888888'),
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'StoryBody',
        parent=styles['Normal'],
        fontSize=12,
        leading=18,
        textColor=colors.HexColor('#333333'),
        spaceAfter=12
    )

    story = []
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 0.3 * inch))

    for scene in scenes:
        story.append(Paragraph(f"SCENE {scene['scene_number']}", scene_number_style))
        story.append(Paragraph(scene['title'], scene_title_style))
        story.append(Paragraph(scene['story'], body_style))

        # Add image if available
        if 'image_bytes' in scene and scene['image_bytes']:
            img_buffer = io.BytesIO(scene['image_bytes'])
            img = RLImage(img_buffer, width=4 * inch, height=3 * inch)
            story.append(img)

        story.append(Spacer(1, 0.2 * inch))
        story.append(PageBreak())

    doc.build(story)
    buffer.seek(0)
    return buffer.read()