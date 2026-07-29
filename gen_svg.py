import sys

# Read the base64 photo data
with open('avatar_b64.txt', 'r') as f:
    PHOTO_B64 = f.read().strip()

IMAGE_HREF = f"data:image/jpeg;base64,{PHOTO_B64}"

def generate_svg(mode):
    """Generate either 'dark' or 'light' SVG."""
    is_dark = mode == 'dark'

    # Color scheme
    if is_dark:
        bg1, bg2 = '#030712', '#050b18'
        panel1a, panel1b = '#0F172A', '#0a0f1e'
        panel2a, panel2b = '#0d1526', '#0F172A'
        header_bg = 'rgba(255,255,255,0.04)'
        border_color = 'rgba(255,255,255,0.08)'
        text_primary = '#F8FAFC'
        text_secondary = '#94A3B8'
        text_muted = '#64748B'
        text_dim = '#4B5563'
        glass_top = 'rgba(255,255,255,0.05)'
        glass_mid = 'rgba(255,255,255,0.01)'
        accent1 = '#7C3AED'
        accent2 = '#22D3EE'
        accent3 = '#10B981'
        glow1_matrix = '0 0 0 0 0.49 0 0 0 0 0.23 0 0 0 0 0.93 0 0 0 0.8 0'
        glow2_matrix = '0 0 0 0 0.13 0 0 0 0 0.83 0 0 0 0 0.93 0 0 0 0.8 0'
        glow3_matrix = '0 0 0 0 0.06 0 0 0 0 0.72 0 0 0 0 0.51 0 0 0 0.8 0'
        glow_std = '3'
        pill_opacity = '0.25'
        pill_stroke_opacity = '0.45'
        shimmer_opacity = '0.8'
        outer_opacity = '0.35'
        bg_glow_opacity = '0.07'
        particle_opacity = '0.7'
        avatar_glow_color = 'rgba(34,211,238,0.25)'
        avatar_ring_color = 'rgba(34,211,238,0.4)'
        divider_color = 'rgba(255,255,255,0.07)'
        social_bg1 = 'rgba(34,211,238,0.08)'
        social_border1 = 'rgba(34,211,238,0.35)'
        social_bg2 = 'rgba(16,185,129,0.08)'
        social_border2 = 'rgba(16,185,129,0.35)'
        social_bg3 = 'rgba(124,58,237,0.08)'
        social_border3 = 'rgba(124,58,237,0.35)'
    else:
        bg1, bg2 = '#FFFFFF', '#F1F5F9'
        panel1a, panel1b = '#F8FAFC', '#EEF2FF'
        panel2a, panel2b = '#FFFFFF', '#F8FAFC'
        header_bg = 'rgba(15,23,42,0.03)'
        border_color = 'rgba(15,23,42,0.09)'
        text_primary = '#0F172A'
        text_secondary = '#475569'
        text_muted = '#64748B'
        text_dim = '#94A3B8'
        glass_top = 'rgba(255,255,255,0.7)'
        glass_mid = 'rgba(255,255,255,0.2)'
        accent1 = '#2563EB'
        accent2 = '#06B6D4'
        accent3 = '#10B981'
        glow1_matrix = '0 0 0 0 0.15 0 0 0 0 0.39 0 0 0 0 0.92 0 0 0 0.35 0'
        glow2_matrix = '0 0 0 0 0.02 0 0 0 0 0.71 0 0 0 0 0.83 0 0 0 0.35 0'
        glow3_matrix = '0 0 0 0 0.06 0 0 0 0 0.72 0 0 0 0 0.51 0 0 0 0.35 0'
        glow_std = '2'
        pill_opacity = '0.12'
        pill_stroke_opacity = '0.30'
        shimmer_opacity = '0.8'
        outer_opacity = '0.30'
        bg_glow_opacity = '0.04'
        particle_opacity = '0.35'
        avatar_glow_color = 'rgba(6,182,212,0.18)'
        avatar_ring_color = 'rgba(6,182,212,0.35)'
        avatar_ring_colors = f'rgba(6,182,212,0.35);rgba(37,99,235,0.45);rgba(16,185,129,0.35);rgba(6,182,212,0.35)'
        divider_color = 'rgba(15,23,42,0.07)'
        social_bg1 = 'rgba(37,99,235,0.08)'
        social_border1 = 'rgba(37,99,235,0.28)'
        social_bg2 = 'rgba(16,185,129,0.08)'
        social_border2 = 'rgba(16,185,129,0.28)'
        social_bg3 = 'rgba(6,182,212,0.08)'
        social_border3 = 'rgba(6,182,212,0.28)'

    if is_dark:
        avatar_ring_colors = f'rgba(34,211,238,0.4);rgba(124,58,237,0.5);rgba(16,185,129,0.4);rgba(34,211,238,0.4)'
    else:
        avatar_ring_colors = f'rgba(6,182,212,0.35);rgba(37,99,235,0.45);rgba(16,185,129,0.35);rgba(6,182,212,0.35)'

    # Shimmer colors
    if is_dark:
        sh1, sh2, sh3 = 'rgba(124,58,237,', 'rgba(34,211,238,', 'rgba(16,185,129,'
    else:
        sh1, sh2, sh3 = 'rgba(37,99,235,', 'rgba(6,182,212,', 'rgba(16,185,129,'

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1180 610" width="1180" height="610">
  <defs>
    <style>text {{ font-family: 'Courier New', Courier, monospace; }}</style>

    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/><stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <linearGradient id="lp" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{panel1a}"/><stop offset="100%" stop-color="{panel1b}"/>
    </linearGradient>
    <linearGradient id="rp" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{panel2a}"/><stop offset="100%" stop-color="{panel2b}"/>
    </linearGradient>
    <linearGradient id="ag" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent1}"><animate attributeName="stop-color" values="{accent1};{accent2};{accent3};{accent1}" dur="5s" repeatCount="indefinite"/></stop>
      <stop offset="50%" stop-color="{accent2}"><animate attributeName="stop-color" values="{accent2};{accent3};{accent1};{accent2}" dur="5s" repeatCount="indefinite"/></stop>
      <stop offset="100%" stop-color="{accent3}"><animate attributeName="stop-color" values="{accent3};{accent1};{accent2};{accent3}" dur="5s" repeatCount="indefinite"/></stop>
    </linearGradient>
    <linearGradient id="ng" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent1}"><animate attributeName="stop-color" values="{accent1};{accent2};{accent3};{accent1}" dur="4s" repeatCount="indefinite"/></stop>
      <stop offset="100%" stop-color="{accent2}"><animate attributeName="stop-color" values="{accent2};{accent3};{accent1};{accent2}" dur="4s" repeatCount="indefinite"/></stop>
    </linearGradient>
    <radialGradient id="avGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{avatar_glow_color}"/><stop offset="100%" stop-color="rgba(0,0,0,0)"/>
    </radialGradient>
    <filter id="g1" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="{glow_std}" result="b"/><feColorMatrix in="b" type="matrix" values="{glow1_matrix}" result="c"/><feMerge><feMergeNode in="c"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="g2" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="{glow_std}" result="b"/><feColorMatrix in="b" type="matrix" values="{glow2_matrix}" result="c"/><feMerge><feMergeNode in="c"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="g3" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="{glow_std}" result="b"/><feColorMatrix in="b" type="matrix" values="{glow3_matrix}" result="c"/><feMerge><feMergeNode in="c"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="avBlur" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur in="SourceGraphic" stdDeviation="12"/></filter>
    <filter id="bgB" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur in="SourceGraphic" stdDeviation="50"/></filter>
    <filter id="nGlow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur in="SourceGraphic" stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <linearGradient id="gl" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{glass_top}"/><stop offset="35%" stop-color="{glass_mid}"/><stop offset="100%" stop-color="rgba(255,255,255,0)"/>
    </linearGradient>
    <linearGradient id="sh" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{sh1}0)"/><stop offset="35%" stop-color="{sh1}0.6)"/><stop offset="50%" stop-color="{sh2}0.85)"/><stop offset="65%" stop-color="{sh3}0.6)"/><stop offset="100%" stop-color="{sh3}0)"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0;-1 0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="p1" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="{sh1}{pill_opacity})"/><stop offset="100%" stop-color="{sh2}0.18)"/></linearGradient>
    <linearGradient id="p2" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="{sh2}0.18)"/><stop offset="100%" stop-color="{sh3}{pill_opacity})"/></linearGradient>
    <linearGradient id="p3" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="{sh3}0.18)"/><stop offset="100%" stop-color="{sh1}{pill_opacity})"/></linearGradient>
    <clipPath id="mc"><rect width="1180" height="610" rx="20"/></clipPath>
    <clipPath id="lc"><rect x="16" y="16" width="422" height="578" rx="14"/></clipPath>
    <clipPath id="rc"><rect x="450" y="16" width="714" height="578" rx="14"/></clipPath>
    <clipPath id="ac"><circle cx="227" cy="250" r="110"/></clipPath>
  </defs>

  <g clip-path="url(#mc)">
    <rect width="1180" height="610" fill="url(#bgGrad)"/>

    <!-- Ambient orbs -->
    <ellipse cx="180" cy="200" rx="260" ry="230" fill="{accent1}" opacity="{bg_glow_opacity}" filter="url(#bgB)"><animate attributeName="cy" values="200;260;200" dur="9s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="750" cy="80" rx="330" ry="250" fill="{accent2}" opacity="0.05" filter="url(#bgB)"><animate attributeName="cy" values="80;140;80" dur="11s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="1080" cy="480" rx="210" ry="200" fill="{accent3}" opacity="0.05" filter="url(#bgB)"><animate attributeName="cy" values="480;420;480" dur="8s" repeatCount="indefinite"/></ellipse>

    <!-- Particles -->
    <circle cx="90" cy="560" r="1.5" fill="{accent2}" opacity="0"><animate attributeName="cy" values="560;40" dur="14s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;{particle_opacity};{particle_opacity};0" keyTimes="0;0.1;0.9;1" dur="14s" repeatCount="indefinite"/></circle>
    <circle cx="380" cy="560" r="1.5" fill="{accent3}" opacity="0"><animate attributeName="cy" values="560;40" dur="16s" repeatCount="indefinite" begin="4s"/><animate attributeName="opacity" values="0;{particle_opacity};{particle_opacity};0" keyTimes="0;0.1;0.9;1" dur="16s" repeatCount="indefinite" begin="4s"/></circle>
    <circle cx="620" cy="560" r="1" fill="{accent1}" opacity="0"><animate attributeName="cy" values="560;40" dur="12s" repeatCount="indefinite" begin="1s"/><animate attributeName="opacity" values="0;0.5;0.5;0" keyTimes="0;0.1;0.9;1" dur="12s" repeatCount="indefinite" begin="1s"/></circle>
    <circle cx="900" cy="560" r="1.5" fill="{accent2}" opacity="0"><animate attributeName="cy" values="560;40" dur="13s" repeatCount="indefinite" begin="3s"/><animate attributeName="opacity" values="0;0.6;0.6;0" keyTimes="0;0.1;0.9;1" dur="13s" repeatCount="indefinite" begin="3s"/></circle>

    <!-- LEFT PANEL -->
    <rect x="16" y="16" width="422" height="578" rx="14" fill="url(#lp)" stroke="{border_color}" stroke-width="1"/>
    {'<rect x="20" y="20" width="418" height="574" rx="14" fill="none" stroke="rgba(15,23,42,0.04)" stroke-width="3"/>' if not is_dark else ''}
    <rect x="16" y="16" width="422" height="200" rx="14" fill="url(#gl)" clip-path="url(#lc)"/>
    <rect x="16" y="16" width="422" height="38" rx="14" fill="{header_bg}"/>
    <rect x="16" y="40" width="422" height="14" fill="{header_bg}"/>
    <circle cx="42" cy="35" r="6" fill="#FF5F56"/><circle cx="62" cy="35" r="6" fill="#FFBD2E"/><circle cx="82" cy="35" r="6" fill="#27C93F"/>
    <text x="227" y="40" text-anchor="middle" font-size="10" fill="{text_dim}">mueez@Mohammeds-MacBook-Pro ~ %</text>

    <!-- Scanline -->
    <rect x="16" y="54" width="422" height="2" fill="{accent2}" opacity="0.08" clip-path="url(#lc)"><animate attributeName="y" values="54;594;54" dur="4s" repeatCount="indefinite"/></rect>

    <g clip-path="url(#lc)">
      <!-- Photo glow pulse -->
      <circle cx="227" cy="250" r="128" fill="url(#avGlow)" filter="url(#avBlur)"><animate attributeName="r" values="122;138;122" dur="4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.5;1;0.5" dur="4s" repeatCount="indefinite"/></circle>

      <!-- Photo background circle -->
      <circle cx="227" cy="250" r="110" fill="rgba(0,0,0,0.3)" stroke="{avatar_ring_color}" stroke-width="2"><animate attributeName="stroke" values="{avatar_ring_colors}" dur="5s" repeatCount="indefinite"/></circle>

      <!-- ACTUAL PHOTO -->
      <g clip-path="url(#ac)">
        <image x="117" y="140" width="220" height="220" preserveAspectRatio="xMidYMid slice" href="{IMAGE_HREF}">
          <animateTransform attributeName="transform" type="translate" values="0,0;0,-4;0,0" dur="5s" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" repeatCount="indefinite"/>
        </image>
      </g>

      <!-- Animated ring -->
      <circle cx="227" cy="250" r="110" fill="none" stroke="url(#ag)" stroke-width="2.5" opacity="0.6" stroke-dasharray="120 572"><animateTransform attributeName="transform" type="rotate" values="0 227 250;360 227 250" dur="8s" repeatCount="indefinite"/></circle>
      <circle cx="227" cy="250" r="116" fill="none" stroke="url(#ag)" stroke-width="1" opacity="0.3" stroke-dasharray="60 672"><animateTransform attributeName="transform" type="rotate" values="360 227 250;0 227 250" dur="12s" repeatCount="indefinite"/></circle>

      <!-- Name below -->
      <text x="227" y="390" text-anchor="middle" font-size="14" font-weight="bold" fill="url(#ag)" filter="url(#g2)" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.6s" begin="2s" fill="freeze"/>Mohammed Huzaif Mueez</text>
      <text x="227" y="412" text-anchor="middle" font-size="10" fill="{text_secondary}" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="2.4s" fill="freeze"/>B.E. CS (AI &amp; ML) · MIT Mysore</text>

      <!-- Status -->
      <text x="40" y="446" font-size="10" fill="{accent3}" filter="url(#g3)" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="2.7s" fill="freeze"/>● SYSTEM ONLINE</text>
      <text x="40" y="464" font-size="10" fill="{accent2}" filter="url(#g2)" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="3s" fill="freeze"/>▶ AI/ML ENGINEER</text>
      <text x="40" y="482" font-size="10" fill="{accent1}" filter="url(#g1)" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="3.3s" fill="freeze"/>◆ MYSORE, INDIA · 2023–2027</text>
      <text x="40" y="500" font-size="10" fill="{text_secondary}" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="3.6s" fill="freeze"/>░ OPEN TO OPPORTUNITIES</text>

      <!-- Cursor -->
      <rect x="40" y="516" width="7" height="13" fill="{accent2}" filter="url(#g2)" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.1s" begin="4s" fill="freeze"/><animate attributeName="opacity" values="1;0;1;0" dur="1s" repeatCount="indefinite" begin="4.5s"/></rect>
    </g>
    <rect x="16" y="16" width="422" height="578" rx="14" fill="none" stroke="url(#sh)" stroke-width="1.5" opacity="{shimmer_opacity}"/>

    <!-- RIGHT PANEL -->
    <rect x="450" y="16" width="714" height="578" rx="14" fill="url(#rp)" stroke="{border_color}" stroke-width="1"/>
    {'<rect x="454" y="20" width="710" height="574" rx="14" fill="none" stroke="rgba(15,23,42,0.04)" stroke-width="3"/>' if not is_dark else ''}
    <rect x="450" y="16" width="714" height="200" rx="14" fill="url(#gl)" clip-path="url(#rc)"/>
    <rect x="450" y="16" width="714" height="38" rx="14" fill="{header_bg}"/>
    <rect x="450" y="40" width="714" height="14" fill="{header_bg}"/>
    <circle cx="476" cy="35" r="6" fill="#FF5F56"/><circle cx="496" cy="35" r="6" fill="#FFBD2E"/><circle cx="516" cy="35" r="6" fill="#27C93F"/>
    <text x="807" y="40" text-anchor="middle" font-size="10" fill="{text_dim}">profile.config — Mohammed Huzaif Mueez</text>

    <g clip-path="url(#rc)">
      <!-- Terminal prompt -->
      <text x="470" y="82" font-size="11.5" fill="{accent1}" filter="url(#g1)" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="0.3s" fill="freeze"/>mueez@Mohammeds-MacBook-Pro</text>
      <text x="706" y="82" font-size="11.5" fill="{text_secondary}" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="0.3s" fill="freeze"/>~ %</text>
      <text x="732" y="82" font-size="11.5" fill="{accent3}" filter="url(#g3)" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="0.6s" fill="freeze"/>whoami</text>

      <!-- Greeting -->
      <text x="470" y="120" font-size="28" font-weight="bold" fill="{text_primary}" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1s" fill="freeze"/>Hi 👋  I'm</text>

      <!-- Name -->
      <text x="470" y="162" font-size="32" font-weight="bold" fill="url(#ng)" filter="url(#nGlow)" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.6s" begin="1.5s" fill="freeze"/>Mohammed Huzaif Mueez</text>

      <!-- Roles -->
      <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="2s" fill="freeze"/>
        <text x="470" y="192" font-size="16" fill="{accent2}" filter="url(#g2)"><animate attributeName="visibility" values="visible;hidden;hidden;hidden;visible;hidden;hidden;hidden" dur="12s" repeatCount="indefinite" begin="2.5s"/>AI/ML Engineer_</text>
        <text x="470" y="192" font-size="16" fill="{accent1}" filter="url(#g1)"><animate attributeName="visibility" values="hidden;visible;hidden;hidden;hidden;visible;hidden;hidden" dur="12s" repeatCount="indefinite" begin="2.5s"/>Full Stack Developer_</text>
        <text x="470" y="192" font-size="16" fill="{accent3}" filter="url(#g3)"><animate attributeName="visibility" values="hidden;hidden;visible;hidden;hidden;hidden;visible;hidden" dur="12s" repeatCount="indefinite" begin="2.5s"/>Drone &amp; Robotics Builder_</text>
        <text x="470" y="192" font-size="16" fill="{accent2}" filter="url(#g2)"><animate attributeName="visibility" values="hidden;hidden;hidden;visible;hidden;hidden;hidden;visible" dur="12s" repeatCount="indefinite" begin="2.5s"/>Generative AI Enthusiast_</text>
      </g>

      <line x1="470" y1="210" x2="1148" y2="210" stroke="{divider_color}" stroke-width="1" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="2.2s" fill="freeze"/></line>

      <!-- Info rows -->
      <g font-size="12" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="2.4s" fill="freeze"/>
        <text x="470" y="236" fill="{text_secondary}">📍</text><text x="494" y="236" fill="{text_muted}">Location </text><text x="582" y="236" fill="{text_primary}">Mysore, Karnataka, India</text>
        <text x="470" y="260" fill="{text_secondary}">🎓</text><text x="494" y="260" fill="{text_muted}">Education</text><text x="582" y="260" fill="{text_primary}">B.E. CS (AI &amp; ML) · MIT Mysore · 2023–2027</text>
        <text x="470" y="284" fill="{text_secondary}">🔭</text><text x="494" y="284" fill="{text_muted}">Focus    </text><text x="582" y="284" fill="{text_primary}">GenAI · Computer Vision · Autonomous Drones</text>
        <text x="470" y="308" fill="{text_secondary}">🏆</text><text x="494" y="308" fill="{text_muted}">Awards   </text><text x="582" y="308" fill="{accent3}" filter="url(#g3)">1st ML Quiz · 3rd DroneX · NLC Presenter</text>
        <text x="470" y="332" fill="{text_secondary}">✉</text><text x="494" y="332" fill="{text_muted}">Email    </text><text x="582" y="332" fill="{accent2}" filter="url(#g2)">mueezmueez9@gmail.com</text>
      </g>

      <line x1="470" y1="350" x2="1148" y2="350" stroke="{divider_color}" stroke-width="1" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="2.8s" fill="freeze"/></line>

      <!-- Tech Stack -->
      <text x="470" y="370" font-size="10" fill="{text_dim}" letter-spacing="3" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="3s" fill="freeze"/>TECH STACK</text>

      <!-- Row 1 -->
      <g font-size="10" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="3.3s" fill="freeze"/>
        <rect x="470" y="380" width="58" height="21" rx="10.5" fill="url(#p1)" stroke="{sh1}{pill_stroke_opacity})" stroke-width="1"/><text x="499" y="395" text-anchor="middle" fill="{accent2}">Python</text>
        <rect x="536" y="380" width="60" height="21" rx="10.5" fill="url(#p2)" stroke="{sh2}{pill_stroke_opacity})" stroke-width="1"/><text x="566" y="395" text-anchor="middle" fill="{accent2}">PyTorch</text>
        <rect x="604" y="380" width="78" height="21" rx="10.5" fill="url(#p3)" stroke="{sh3}{pill_stroke_opacity})" stroke-width="1"/><text x="643" y="395" text-anchor="middle" fill="{accent3}">TensorFlow</text>
        <rect x="690" y="380" width="64" height="21" rx="10.5" fill="url(#p1)" stroke="{sh1}{pill_stroke_opacity})" stroke-width="1"/><text x="722" y="395" text-anchor="middle" fill="{accent2}">React.js</text>
        <rect x="762" y="380" width="58" height="21" rx="10.5" fill="url(#p2)" stroke="{sh2}{pill_stroke_opacity})" stroke-width="1"/><text x="791" y="395" text-anchor="middle" fill="{accent1}">Next.js</text>
        <rect x="828" y="380" width="58" height="21" rx="10.5" fill="url(#p3)" stroke="{sh3}{pill_stroke_opacity})" stroke-width="1"/><text x="857" y="395" text-anchor="middle" fill="{accent3}">FastAPI</text>
        <rect x="894" y="380" width="56" height="21" rx="10.5" fill="url(#p1)" stroke="{sh1}{pill_stroke_opacity})" stroke-width="1"/><text x="922" y="395" text-anchor="middle" fill="{accent2}">Django</text>
        <rect x="958" y="380" width="56" height="21" rx="10.5" fill="url(#p2)" stroke="{sh2}{pill_stroke_opacity})" stroke-width="1"/><text x="986" y="395" text-anchor="middle" fill="{accent1}">Docker</text>
        <rect x="1022" y="380" width="34" height="21" rx="10.5" fill="url(#p3)" stroke="{sh3}{pill_stroke_opacity})" stroke-width="1"/><text x="1039" y="395" text-anchor="middle" fill="{accent3}">Git</text>
      </g>

      <!-- Row 2 -->
      <g font-size="10" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="3.6s" fill="freeze"/>
        <rect x="470" y="409" width="78" height="21" rx="10.5" fill="url(#p3)" stroke="{sh3}{pill_stroke_opacity})" stroke-width="1"/><text x="509" y="424" text-anchor="middle" fill="{accent3}">LangChain</text>
        <rect x="556" y="409" width="64" height="21" rx="10.5" fill="url(#p1)" stroke="{sh1}{pill_stroke_opacity})" stroke-width="1"/><text x="588" y="424" text-anchor="middle" fill="{accent1}">OpenCV</text>
        <rect x="628" y="409" width="72" height="21" rx="10.5" fill="url(#p2)" stroke="{sh2}{pill_stroke_opacity})" stroke-width="1"/><text x="664" y="424" text-anchor="middle" fill="{accent2}">MongoDB</text>
        <rect x="708" y="409" width="84" height="21" rx="10.5" fill="url(#p3)" stroke="{sh3}{pill_stroke_opacity})" stroke-width="1"/><text x="750" y="424" text-anchor="middle" fill="{accent3}">PostgreSQL</text>
        <rect x="800" y="409" width="84" height="21" rx="10.5" fill="url(#p1)" stroke="{sh1}{pill_stroke_opacity})" stroke-width="1"/><text x="842" y="424" text-anchor="middle" fill="{accent2}">Gemini API</text>
        <rect x="892" y="409" width="78" height="21" rx="10.5" fill="url(#p2)" stroke="{sh2}{pill_stroke_opacity})" stroke-width="1"/><text x="931" y="424" text-anchor="middle" fill="{accent1}">LangGraph</text>
        <rect x="978" y="409" width="80" height="21" rx="10.5" fill="url(#p3)" stroke="{sh3}{pill_stroke_opacity})" stroke-width="1"/><text x="1018" y="424" text-anchor="middle" fill="{accent3}">Scikit-learn</text>
      </g>

      <line x1="470" y1="444" x2="1148" y2="444" stroke="{divider_color}" stroke-width="1" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="3.9s" fill="freeze"/></line>

      <text x="470" y="464" font-size="10" fill="{text_dim}" letter-spacing="3" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="4.1s" fill="freeze"/>CONNECT</text>

      <!-- Social -->
      <g font-size="11" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="4.4s" fill="freeze"/>
        <rect x="470" y="474" width="128" height="32" rx="16" fill="{social_bg1}" stroke="{social_border1}" stroke-width="1"/><text x="534" y="495" text-anchor="middle" fill="{accent2}">in  LinkedIn</text>
        <rect x="610" y="474" width="112" height="32" rx="16" fill="{social_bg2}" stroke="{social_border2}" stroke-width="1"/><text x="666" y="495" text-anchor="middle" fill="{accent3}">✉  Email</text>
        <rect x="734" y="474" width="190" height="32" rx="16" fill="{social_bg3}" stroke="{social_border3}" stroke-width="1"/><text x="829" y="495" text-anchor="middle" fill="{accent1}">☁  Oracle GenAI Certified</text>
      </g>

      <!-- Bottom prompt -->
      <text x="470" y="540" font-size="11.5" fill="{accent1}" filter="url(#g1)" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="4.8s" fill="freeze"/>mueez@Mohammeds-MacBook-Pro</text>
      <text x="706" y="540" font-size="11.5" fill="{text_secondary}" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="4.8s" fill="freeze"/>~ %</text>
      <text x="732" y="540" font-size="11.5" fill="{accent3}" filter="url(#g3)" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="5.1s" fill="freeze"/>building --the-future</text>
      <rect x="860" y="528" width="8" height="14" fill="{accent2}" filter="url(#g2)" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.1s" begin="5.5s" fill="freeze"/><animate attributeName="opacity" values="1;0;1;0" dur="1s" repeatCount="indefinite" begin="6s"/></rect>
      <text x="1140" y="582" text-anchor="end" font-size="9" fill="{text_dim}" opacity="0.3">v2.0.26</text>
    </g>

    <rect x="450" y="16" width="714" height="578" rx="14" fill="none" stroke="url(#sh)" stroke-width="1.5" opacity="0.6"/>
    <rect width="1180" height="610" rx="20" fill="none" stroke="url(#ag)" stroke-width="1.5" opacity="{outer_opacity}"/>
  </g>
</svg>'''
    return svg


# Generate both
for mode in ['dark', 'light']:
    svg_content = generate_svg(mode)
    with open(f'{mode}.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f'{mode}.svg written ({len(svg_content)} bytes)')

print('Done!')
