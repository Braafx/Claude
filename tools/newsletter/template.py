"""HTML email template for the daily art newsletter."""
from __future__ import annotations

from .content import NewsletterContent


def render(c: NewsletterContent) -> str:
    """Render newsletter content as a mobile-friendly HTML email."""
    bonus_html = _render_bonus(c.bonus)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Daily Art Brief — {c.date}</title>
</head>
<body style="margin:0;padding:0;background:#0d1117;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;color:#e6edf3;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0d1117;padding:20px 0;">
    <tr><td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">

        <!-- HEADER -->
        <tr><td style="background:#161b22;border-radius:12px 12px 0 0;padding:28px 32px;border-bottom:2px solid #f4a261;">
          <p style="margin:0;font-size:12px;color:#8b949e;letter-spacing:2px;text-transform:uppercase;">Daily Art Brief</p>
          <h1 style="margin:6px 0 0;font-size:26px;font-weight:700;color:#f0f6fc;">{c.date}</h1>
          <p style="margin:8px 0 0;font-size:14px;color:#8b949e;">Your daily concept art coaching drop.</p>
        </td></tr>

        <!-- COACH'S NOTE -->
        <tr><td style="background:#1c2128;padding:24px 32px;border-left:3px solid #f4a261;">
          <p style="margin:0 0 8px;font-size:11px;color:#f4a261;letter-spacing:2px;text-transform:uppercase;">Coach's Note</p>
          <p style="margin:0;font-size:15px;line-height:1.6;color:#e6edf3;">{c.coach_note}</p>
        </td></tr>

        <!-- DIVIDER -->
        <tr><td style="background:#0d1117;height:8px;"></td></tr>

        <!-- REFERENCE OF THE DAY -->
        <tr><td style="background:#161b22;border-radius:8px;padding:24px 32px;">
          <p style="margin:0 0 12px;font-size:11px;color:#79c0ff;letter-spacing:2px;text-transform:uppercase;">Reference of the Day</p>
          <p style="margin:0 0 14px;font-size:13px;color:#8b949e;">Query: <strong style="color:#e6edf3;">{c.reference_query}</strong></p>
          <a href="{c.reference_url}" style="display:block;">
            <img src="{c.reference_url}" width="536" alt="Daily Reference — {c.reference_query}"
              style="width:100%;max-width:536px;border-radius:6px;display:block;">
          </a>
          <p style="margin:10px 0 0;font-size:12px;color:#8b949e;">
            Click image to open full size. Use this for studies, value practice, or texture reference.
          </p>
        </td></tr>

        <!-- DIVIDER -->
        <tr><td style="background:#0d1117;height:8px;"></td></tr>

        <!-- CONCEPT ART THROWBACK -->
        <tr><td style="background:#161b22;border-radius:8px;padding:24px 32px;">
          <p style="margin:0 0 4px;font-size:11px;color:#d2a8ff;letter-spacing:2px;text-transform:uppercase;">Concept Art Throwback</p>
          <h2 style="margin:0 0 4px;font-size:18px;color:#f0f6fc;">{c.throwback['game']}</h2>
          <p style="margin:0 0 12px;font-size:13px;color:#8b949e;">{c.throwback['studio']} &nbsp;·&nbsp; {c.throwback['year']} &nbsp;·&nbsp; <em>{c.throwback['style']}</em></p>
          <p style="margin:0 0 12px;font-size:14px;line-height:1.6;color:#e6edf3;">{c.throwback['note']}</p>
          <div style="background:#0d1117;border-radius:6px;padding:14px 16px;border-left:3px solid #d2a8ff;">
            <p style="margin:0 0 4px;font-size:11px;color:#d2a8ff;text-transform:uppercase;letter-spacing:1px;">Design Lesson</p>
            <p style="margin:0;font-size:14px;line-height:1.5;color:#c9d1d9;">{c.throwback['design_lesson']}</p>
          </div>
          <p style="margin:12px 0 0;">
            <a href="{c.throwback['find_at']}" style="font-size:13px;color:#79c0ff;">Find concept art →</a>
          </p>
        </td></tr>

        <!-- DIVIDER -->
        <tr><td style="background:#0d1117;height:8px;"></td></tr>

        <!-- TUTORIAL PICK -->
        <tr><td style="background:#161b22;border-radius:8px;padding:24px 32px;">
          <p style="margin:0 0 4px;font-size:11px;color:#56d364;letter-spacing:2px;text-transform:uppercase;">Tutorial Pick</p>
          <h2 style="margin:0 0 4px;font-size:18px;color:#f0f6fc;">{c.tutorial['title']}</h2>
          <p style="margin:0 0 8px;font-size:13px;color:#8b949e;">{c.tutorial['author']} &nbsp;·&nbsp; {c.tutorial['format']} &nbsp;·&nbsp; Level: {c.tutorial['level']}</p>
          <p style="margin:0 0 14px;font-size:14px;line-height:1.6;color:#e6edf3;">{c.tutorial['note']}</p>
          <a href="{c.tutorial['url']}"
            style="display:inline-block;background:#238636;color:#f0f6fc;text-decoration:none;padding:10px 20px;border-radius:6px;font-size:14px;font-weight:600;">
            Open Tutorial →
          </a>
        </td></tr>

        <!-- DIVIDER -->
        <tr><td style="background:#0d1117;height:8px;"></td></tr>

        <!-- FREE BRUSH -->
        <tr><td style="background:#161b22;border-radius:8px;padding:24px 32px;">
          <p style="margin:0 0 4px;font-size:11px;color:#ffa657;letter-spacing:2px;text-transform:uppercase;">Free Brush Pick</p>
          <h2 style="margin:0 0 4px;font-size:18px;color:#f0f6fc;">{c.brush['name']}</h2>
          <p style="margin:0 0 8px;font-size:13px;color:#8b949e;">App: {c.brush['app']}</p>
          <p style="margin:0 0 14px;font-size:14px;line-height:1.6;color:#e6edf3;">{c.brush['note']}</p>
          <a href="{c.brush['url']}"
            style="display:inline-block;background:#1f6feb;color:#f0f6fc;text-decoration:none;padding:10px 20px;border-radius:6px;font-size:14px;font-weight:600;">
            Get Brush →
          </a>
        </td></tr>

        <!-- DIVIDER -->
        <tr><td style="background:#0d1117;height:8px;"></td></tr>

        <!-- BONUS -->
        <tr><td style="background:#161b22;border-radius:8px;padding:24px 32px;">
          <p style="margin:0 0 4px;font-size:11px;color:#f85149;letter-spacing:2px;text-transform:uppercase;">Today's Bonus</p>
          {bonus_html}
        </td></tr>

        <!-- FOOTER -->
        <tr><td style="background:#161b22;border-radius:0 0 12px 12px;padding:20px 32px;border-top:1px solid #30363d;margin-top:8px;">
          <p style="margin:0;font-size:12px;color:#8b949e;text-align:center;">
            Your daily art coaching drop. Generated by your Claude Code workspace.<br>
            <strong style="color:#f4a261;">Keep making things. The portfolio builds itself.</strong>
          </p>
        </td></tr>

      </table>
    </td></tr>
  </table>
</body>
</html>"""


def _render_bonus(bonus: dict[str, str]) -> str:
    title = bonus.get("title", "Bonus")
    content = bonus.get("content", "")
    bonus_type = bonus.get("type", "")

    icon_map = {
        "palette_challenge": "🎨",
        "artist_to_study": "👁️",
        "quick_exercise": "⚡",
        "industry_fact": "📌",
        "social_tip": "📣",
        "random_challenge": "🎯",
    }
    icon = icon_map.get(bonus_type, "✨")
    badge_colour = {
        "palette_challenge": "#d2a8ff",
        "artist_to_study": "#79c0ff",
        "quick_exercise": "#56d364",
        "industry_fact": "#ffa657",
        "social_tip": "#f4a261",
        "random_challenge": "#f85149",
    }.get(bonus_type, "#e6edf3")

    return f"""
      <span style="display:inline-block;background:{badge_colour}22;color:{badge_colour};
        font-size:11px;padding:2px 8px;border-radius:4px;text-transform:uppercase;
        letter-spacing:1px;margin-bottom:10px;">{bonus_type.replace('_', ' ')}</span>
      <h2 style="margin:0 0 10px;font-size:17px;color:#f0f6fc;">{icon} {title}</h2>
      <p style="margin:0;font-size:14px;line-height:1.6;color:#e6edf3;">{content}</p>
    """
