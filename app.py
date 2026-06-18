import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Simulador AL: Reação Fotoquímica do AgCl",
    layout="wide",
    page_icon="☀️",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Reset Streamlit defaults */
.stApp {
    font-family: 'Inter', sans-serif;
}

/* Hide default Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Step navigation buttons */
.step-nav {
    display: flex;
    justify-content: center;
    gap: 16px;
    margin: 30px 0;
}
.step-nav button {
    padding: 12px 32px;
    border-radius: 50px;
    border: none;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

/* Progress bar */
.progress-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    margin: 40px auto 50px auto;
    max-width: 900px;
    padding: 0 20px;
}
.progress-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    z-index: 2;
    min-width: 60px;
}
.progress-circle {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 18px;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.progress-circle.active {
    background: linear-gradient(135deg, #FF6B35, #F7C948);
    color: white;
    transform: scale(1.15);
    box-shadow: 0 4px 20px rgba(255, 107, 53, 0.4);
}
.progress-circle.completed {
    background: linear-gradient(135deg, #10B981, #34D399);
    color: white;
    box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
}
.progress-circle.inactive {
    background: #E5E7EB;
    color: #9CA3AF;
}
.progress-label {
    margin-top: 10px;
    font-size: 12px;
    font-weight: 600;
    text-align: center;
    max-width: 110px;
    line-height: 1.3;
}
.progress-label.active { color: #FF6B35; }
.progress-label.completed { color: #10B981; }
.progress-label.inactive { color: #9CA3AF; }
.progress-line {
    flex: 1;
    height: 4px;
    border-radius: 2px;
    margin: 0 -5px;
    position: relative;
    top: -14px;
    z-index: 1;
    transition: background 0.5s ease;
}
.progress-line.completed { background: linear-gradient(90deg, #10B981, #34D399); }
.progress-line.inactive { background: #E5E7EB; }

/* Hero section */
.hero {
    text-align: center;
    padding: 40px 20px 10px 20px;
    animation: fadeInDown 0.8s ease;
}
.hero h1 {
    font-size: 2.8em;
    font-weight: 800;
    background: linear-gradient(135deg, #FF6B35, #F7C948, #FF6B35);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 3s linear infinite;
    margin-bottom: 8px;
}
.hero .subtitle {
    font-size: 1.15em;
    color: #6B7280;
    font-weight: 400;
}

@keyframes shimmer {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
}
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* Content cards */
.content-card {
    background: #FFFFFF !important;
    color: #1F2937 !important;
    border-radius: 20px;
    padding: 36px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.06);
    border: 1px solid #F3F4F6;
    animation: fadeInUp 0.6s ease;
    margin-bottom: 24px;
}
.content-card h2 {
    font-size: 1.6em;
    font-weight: 700;
    color: #1F2937 !important;
    margin-bottom: 16px;
}
.content-card p, .content-card li {
    color: #4B5563 !important;
    line-height: 1.7;
    font-size: 1.05em;
}
.content-card ol, .content-card ul {
    color: #4B5563 !important;
}

/* Info card */
.info-card {
    background: linear-gradient(135deg, #EFF6FF, #DBEAFE) !important;
    color: #1e3a5f !important;
    border: 1px solid #BFDBFE;
    border-radius: 16px;
    padding: 20px 24px;
    margin: 16px 0;
    animation: fadeIn 0.5s ease;
}
.info-card strong { color: #1e3a5f !important; }
.info-card .icon { font-size: 1.4em; margin-right: 8px; }

/* Equation card */
.equation-card {
    background: linear-gradient(135deg, #F0FDF4, #DCFCE7) !important;
    border: 1px solid #BBF7D0;
    border-radius: 16px;
    padding: 24px;
    text-align: center;
    margin: 20px 0;
    font-size: 1.2em;
    font-weight: 500;
    color: #166534 !important;
}

/* Question cards */
.question-card {
    background: #FFFFFF !important;
    border-radius: 16px;
    padding: 28px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.05);
    border-left: 4px solid #FF6B35;
    margin-bottom: 24px;
    animation: fadeInUp 0.6s ease;
}
.question-card h3 {
    color: #1F2937 !important;
    font-weight: 700;
    margin-bottom: 12px;
}
.question-card p {
    color: #4B5563 !important;
    line-height: 1.7;
}

/* Conclusion cards */
.conclusion-item {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    padding: 18px 20px;
    border-radius: 14px;
    margin-bottom: 12px;
    animation: fadeInUp 0.5s ease;
}
.conclusion-item .tube-badge {
    min-width: 50px;
    height: 50px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 18px;
    color: white !important;
    flex-shrink: 0;
}
.conclusion-item .text { flex: 1; }
.conclusion-item .text strong { color: #1F2937 !important; }
.conclusion-item .text p { color: #4B5563 !important; margin: 4px 0 0 0; font-size: 0.95em; line-height: 1.5; }
</style>
""", unsafe_allow_html=True)

# ── State ───────────────────────────────────────────────────────────────────
if "current_step" not in st.session_state:
    st.session_state.current_step = 0  # 0=intro, 1=theory, 2=prep, 3=exposure, 4=results, 5=questions

STEPS = [
    ("Introdução", "👋"),
    ("Teoria", "📖"),
    ("Preparação", "🧪"),
    ("Exposição", "☀️"),
    ("Resultados", "🔍"),
    ("Questões", "📝"),
]

def go_to(step):
    st.session_state.current_step = step

# ── Hero ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>☀️ Reação Fotoquímica do AgCl</h1>
    <p class="subtitle">Atividade Laboratorial · Física e Química A · 10.º Ano</p>
</div>
""", unsafe_allow_html=True)

# ── Progress Bar ────────────────────────────────────────────────────────────
current = st.session_state.current_step

progress_html = '<div class="progress-container">'
for i, (label, emoji) in enumerate(STEPS):
    if i < current:
        cls = "completed"
        icon = "✓"
    elif i == current:
        cls = "active"
        icon = emoji
    else:
        cls = "inactive"
        icon = str(i + 1)

    progress_html += f'''
    <div class="progress-step">
        <div class="progress-circle {cls}">{icon}</div>
        <div class="progress-label {cls}">{label}</div>
    </div>
    '''
    if i < len(STEPS) - 1:
        line_cls = "completed" if i < current else "inactive"
        progress_html += f'<div class="progress-line {line_cls}"></div>'

progress_html += '</div>'
st.markdown(progress_html, unsafe_allow_html=True)


# ── Helper: SVG test tubes ─────────────────────────────────────────────────
def get_darkness(time_mins, filter_type):
    factors = {
        'Alumínio': 0.0005,
        'Celofane Azul': 0.85,
        'Celofane Vermelho': 0.15,
        'Celofane Verde': 0.45,
        'Sem embrulho': 1.0,
    }
    f = factors.get(filter_type, 0.0)
    # The darkening scales with time. At 15 mins it's noticeable, caps near 60.
    d = f * min(time_mins / 60.0, 1.0) * 1.5 
    d = min(d, f) # clamp to max factor for this filter
    v = int(255 - d * (255 - 40))
    return f"rgb({v},{v},{v})"

def render_tubes_html(tubes_data, time_mins, show_wrapper, hide_result=False, animate_removal=False, animate_wrap=False, bg_color="#111827"):
    """
    tubes_data: list of (label, filter_type)
    time_mins: exposure time (0-15+)
    show_wrapper: whether to render the wrapping material over the tube
    hide_result: if True, renders tube liquid as pristine white regardless of time
                 (used during the exposure step so results aren't prematurely revealed)
    animate_removal: if True, applies a removal animation to the wrappers
    animate_wrap: if True, applies an animation where the wrappers slide onto the tubes
    bg_color: background color for the tubes container
    Returns a single HTML block with all 5 SVG tubes side-by-side.
    """
    # When wrappers are shown and we want to hide results, use fully opaque wrappers
    wrapper_styles = {
        'Alumínio': ('rgba(150,150,158,1.0)', 'Alumínio'),
        'Celofane Azul': ('rgba(60,80,220,0.55)', 'Azul'),
        'Celofane Vermelho': ('rgba(220,50,50,0.55)', 'Vermelho'),
        'Celofane Verde': ('rgba(50,190,80,0.55)', 'Verde'),
        'Sem embrulho': ('transparent', '—'),
    }

    cards = ""
    for label, ftype in tubes_data:
        # Hide results during exposure step — show pristine white precipitate
        precip_color = "rgb(248,248,248)" if hide_result else get_darkness(time_mins, ftype)
        w_color, w_label = wrapper_styles.get(ftype, ('transparent', ''))
        show_w = (show_wrapper or animate_removal or animate_wrap) and w_color != 'transparent'

        # SVG tube
        wrapper_rect = ""
        if show_w:
            anim_style = ""
            if animate_removal:
                anim_style = 'style="transform-origin: center; animation: unwrap 1.2s forwards ease-in-out;"'
            elif animate_wrap:
                anim_style = 'style="transform-origin: center; animation: wrap 1.2s forwards ease-in-out;"'
                
            wrapper_rect = f'''
            <g {anim_style}>
                <rect x="18" y="10" width="44" height="168" rx="8" ry="8" fill="{w_color}" />
            '''
            if ftype == 'Alumínio':
                # hatching for aluminium
                wrapper_rect += '''
                <line x1="22" y1="20" x2="58" y2="50" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
                <line x1="22" y1="40" x2="58" y2="70" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
                <line x1="22" y1="60" x2="58" y2="90" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
                <line x1="22" y1="80" x2="58" y2="110" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
                <line x1="22" y1="100" x2="58" y2="130" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
                <line x1="22" y1="120" x2="58" y2="150" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
                <line x1="22" y1="140" x2="58" y2="170" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
                '''
            wrapper_rect += '</g>'

        # Liquid meniscus path
        svg = f'''
        <svg width="80" height="200" viewBox="0 0 80 200" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="glass_{label}" x1="0" y1="0" x2="1" y2="0">
                    <stop offset="0%" stop-color="rgba(255,255,255,0.15)"/>
                    <stop offset="30%" stop-color="rgba(255,255,255,0.05)"/>
                    <stop offset="100%" stop-color="rgba(255,255,255,0.20)"/>
                </linearGradient>
                <linearGradient id="liquid_{label}" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="{precip_color}" stop-opacity="0.7"/>
                    <stop offset="100%" stop-color="{precip_color}" stop-opacity="1"/>
                </linearGradient>
                <filter id="shadow_{label}">
                    <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.10"/>
                </filter>
            </defs>

            <!-- Tube body -->
            <path d="M22,8 L22,148 Q22,178 40,178 Q58,178 58,148 L58,8"
                  fill="url(#glass_{label})" stroke="#b0b8c4" stroke-width="2"
                  filter="url(#shadow_{label})"/>

            <!-- Liquid -->
            <path d="M24,130 Q40,124 56,130 L56,148 Q56,174 40,174 Q24,174 24,148 Z"
                  fill="url(#liquid_{label})" />

            <!-- Glass highlight -->
            <path d="M27,14 L27,145 Q27,168 35,172"
                  fill="none" stroke="rgba(255,255,255,0.45)" stroke-width="2.5"
                  stroke-linecap="round"/>

            <!-- Rim -->
            <ellipse cx="40" cy="8" rx="19" ry="4" fill="none" stroke="#a0a8b4" stroke-width="1.8"/>
            <ellipse cx="40" cy="8" rx="17" ry="3" fill="rgba(200,210,220,0.3)"/>

            {wrapper_rect}
        </svg>
        '''

        badge_colors = {
            'Alumínio': '#6B7280',
            'Celofane Azul': '#3B82F6',
            'Celofane Vermelho': '#EF4444',
            'Celofane Verde': '#22C55E',
            'Sem embrulho': '#F59E0B',
        }
        badge_bg = badge_colors.get(ftype, '#6B7280')

        cards += f'''
        <div style="display:flex; flex-direction:column; align-items:center; animation: fadeInUp 0.6s ease {0.1 * (ord(label) - 64)}s both;">
            <div style="
                font-weight:700; font-size:15px; color:white;
                margin-bottom:8px; font-family:'Inter',sans-serif;
            ">Tubo {label}</div>
            {svg}
            <div style="
                margin-top:10px; padding:4px 14px; border-radius:20px;
                background:{badge_bg}; color:white; font-size:12px;
                font-weight:600; font-family:'Inter',sans-serif;
                letter-spacing:0.3px;
            ">{ftype}</div>
        </div>
        '''

    full_html = f'''
    <div style="
        display: flex;
        justify-content: center;
        align-items: flex-end;
        gap: 36px;
        padding: 30px 10px;
        flex-wrap: wrap;
        background: {bg_color};
        border-radius: 20px;
        transition: background 0.5s ease;
    ">
        {cards}
    </div>
    <style>
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(25px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes unwrap {{
            0% {{ transform: translateY(0); opacity: 1; }}
            30% {{ transform: translateY(-8px); opacity: 1; }}
            100% {{ transform: translateY(80px); opacity: 0; display: none; }}
        }}
        @keyframes wrap {{
            0% {{ transform: translateY(-150px); opacity: 0; }}
            100% {{ transform: translateY(0); opacity: 1; }}
        }}
    </style>
    '''
    return full_html


TUBES = [
    ("A", "Alumínio"),
    ("B", "Celofane Azul"),
    ("C", "Celofane Vermelho"),
    ("D", "Celofane Verde"),
    ("E", "Sem embrulho"),
]

# ── Step 0 – Introdução ────────────────────────────────────────────────────
if current == 0:
    st.markdown("""
    <div class="content-card" style="text-align:center; padding:50px 36px;">
        <h2 style="font-size:1.8em;">Bem-vindo ao Laboratório Virtual! 🔬</h2>
        <p style="max-width:650px; margin:0 auto 24px auto; font-size:1.1em;">
            Nesta atividade laboratorial, vais investigar o <strong>efeito da luz sobre o cloreto de prata (AgCl)</strong>
            — o fenómeno que está na origem da fotografia.
        </p>
        <p style="max-width:600px; margin:0 auto; font-size:1.0em; color:#6B7280;">
            Vais preparar cinco tubos de ensaio com AgCl, embrulhá-los com diferentes materiais,
            expô-los à luz solar e observar o que acontece. Pronto?
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("Começar →", use_container_width=True, type="primary"):
            go_to(1)
            st.rerun()

# ── Step 1 – Enquadramento Teórico ─────────────────────────────────────────
elif current == 1:
    st.markdown("""
    <div class="content-card">
        <h2>📖 Enquadramento Teórico</h2>
        <p>
            Por volta de <strong>1770</strong>, o químico sueco <strong>Carl Scheele</strong> observou que o cloreto de prata
            escurecia quando exposto à luz. Esta descoberta foi fundamental para o desenvolvimento da
            <em>fotografia</em> no século XIX — "photography" significa literalmente <em>escrever com luz</em>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <span class="icon">💡</span>
        <strong>O cloreto de prata (AgCl)</strong> é um sal branco fotossensível. Ao ser exposto à luz visível
        e ultravioleta, sofre uma <strong>reação fotoquímica</strong> — decompõe-se em prata metálica (Ag), que
        provoca o escurecimento, e gás cloro (Cl₂).
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="equation-card">
            <div style="font-size:0.8em; color:#4B5563; margin-bottom:8px; font-weight:600;">Preparação do AgCl</div>
            AgNO₃(aq) + NaCl(aq) → AgCl(s)↓ + NaNO₃(aq)
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="equation-card">
            <div style="font-size:0.8em; color:#4B5563; margin-bottom:8px; font-weight:600;">Reação Fotoquímica</div>
            2 AgCl(s) —<em>luz</em>→ 2 Ag(s) + Cl₂(g)
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="content-card" style="margin-top:8px;">
        <h2>🎯 Objetivo</h2>
        <p>
            Investigar o efeito de <strong>diferentes cores de luz</strong> sobre o cloreto de prata,
            utilizando filtros de celofane coloridos e um controlo com folha de alumínio.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Voltar", use_container_width=True):
            go_to(0)
            st.rerun()
    with col3:
        if st.button("Preparar Tubos →", use_container_width=True, type="primary"):
            go_to(2)
            st.rerun()

# ── Step 2 – Preparação ────────────────────────────────────────────────────
elif current == 2:
    st.markdown("""
    <div class="content-card">
        <h2>🧪 Preparação dos Tubos de Ensaio</h2>
        <p>Seguindo o protocolo experimental:</p>
        <ol style="color:#4B5563; line-height:2;">
            <li>Preparar <strong>cinco tubos de ensaio</strong>.</li>
            <li>Medir <strong>1,0 mL</strong> de solução aquosa de <strong>AgNO₃</strong> (0,010 mol/dm³) para cada tubo.</li>
            <li>Adicionar <strong>1,0 mL</strong> de solução aquosa de <strong>NaCl</strong> (0,010 mol/dm³) a cada tubo.</li>
            <li>Forma-se imediatamente um <strong>precipitado branco</strong> de AgCl.</li>
            <li>Rolhar todos os tubos com <strong>tampas opacas</strong>.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <span class="icon">🧤</span>
        <strong>Segurança:</strong> O nitrato de prata (AgNO₃) provoca manchas escuras na pele e é corrosivo em concentrações elevadas. 
        Usar luvas e manusear com cuidado!
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='text-align:center; color:#4B5563; margin:30px 0 10px 0;'>Todos os tubos contêm precipitado branco de AgCl</h4>", unsafe_allow_html=True)
    components.html(render_tubes_html(TUBES, 0, show_wrapper=False), height=310)

    st.markdown("""
    <div class="content-card" style="margin-top:16px;">
        <h2>📦 Embrulhar os Tubos</h2>
        <p>Cada tubo é agora embrulhado de forma diferente para controlar a luz que atinge o AgCl:</p>
    </div>
    """, unsafe_allow_html=True)

    components.html(render_tubes_html(TUBES, 0, show_wrapper=False, animate_wrap=True), height=310)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Teoria", use_container_width=True):
            go_to(1)
            st.rerun()
    with col3:
        if st.button("Expor à Luz ☀️ →", use_container_width=True, type="primary"):
            go_to(3)
            st.rerun()

# ── Step 3 – Exposição ─────────────────────────────────────────────────────
elif current == 3:
    if st.session_state.get('animating_radiation'):
        # Fullscreen overlay to cover Streamlit UI chrome
        st.markdown("""
        <style>
            header, .stSidebar, [data-testid="stHeader"],
            [data-testid="stToolbar"], [data-testid="stDecoration"],
            [data-testid="stStatusWidget"] { display: none !important; }
            .stApp { background: #1a1a2e !important; }
            section[data-testid="stMain"] { padding: 0 !important; }
            .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }
            .block-container { padding: 0 !important; max-width: 100% !important; }
            iframe { border: none !important; }
        </style>
        """, unsafe_allow_html=True)

        time_exp = st.session_state.get('time_exp', 15)
        tubes_html = render_tubes_html(TUBES, time_exp, show_wrapper=True, hide_result=True)
        
        anim_html = """
        <!DOCTYPE html>
        <html><head><style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            background: #1a1a2e;
            display: flex; flex-direction: column;
            justify-content: center; align-items: center;
            height: 100vh; overflow: hidden;
            font-family: 'Inter', sans-serif;
            animation: bgFlash 3.5s forwards ease-in-out;
        }
        h1 {
            font-size: 2.8em; color: #FDE68A;
            text-shadow: 0 0 30px rgba(253,230,138,0.5);
            animation: pulse 0.8s infinite alternate;
            margin-bottom: 30px; text-align: center;
        }
        .scene { 
            position: relative; display: flex; justify-content: center; 
            align-items: center; width: 100%; max-width: 900px; 
            min-height: 400px;
        }
        .tubes-container { z-index: 10; position: relative; transform: scale(1.15); }
        .em-wave {
            position: absolute; left: -200px;
            animation: emShoot 1.4s linear infinite;
            z-index: 5; opacity: 0;
        }
        .em-wave svg { display: block; }
        @keyframes emShoot {
            0%   { transform: translateX(0); opacity: 0; }
            5%   { opacity: 1; }
            85%  { opacity: 1; }
            100% { transform: translateX(900px); opacity: 0; }
        }
        @keyframes bgFlash {
            0%   { opacity: 0; }
            12%  { opacity: 1; }
            88%  { opacity: 1; }
            100% { opacity: 0; }
        }
        @keyframes pulse {
            0%   { transform: scale(1); opacity: 0.85; }
            100% { transform: scale(1.04); opacity: 1; }
        }
        </style></head><body>
            <h1>☀️ Radiação solar a incidir nos tubos... ☀️</h1>
            <div class="scene">
                <div class="em-wave" style="top:15%; animation-delay:0.0s; animation-duration:1.3s;">
                    <svg width="180" height="26" viewBox="0 0 180 26"><defs><marker id="a1" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="rgba(255,255,255,0.9)"/></marker></defs><path d="M0,13 Q15,0 30,13 T60,13 T90,13 T120,13 T150,13" fill="none" stroke="rgba(255,255,255,0.85)" stroke-width="2" marker-end="url(#a1)"/></svg>
                </div>
                <div class="em-wave" style="top:30%; animation-delay:0.3s; animation-duration:1.5s;">
                    <svg width="180" height="26" viewBox="0 0 180 26"><defs><marker id="a2" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="rgba(255,255,255,0.9)"/></marker></defs><path d="M0,13 Q15,0 30,13 T60,13 T90,13 T120,13 T150,13" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="2" marker-end="url(#a2)"/></svg>
                </div>
                <div class="em-wave" style="top:55%; animation-delay:0.6s; animation-duration:1.4s;">
                    <svg width="180" height="26" viewBox="0 0 180 26"><defs><marker id="a3" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="rgba(255,255,255,0.9)"/></marker></defs><path d="M0,13 Q15,0 30,13 T60,13 T90,13 T120,13 T150,13" fill="none" stroke="rgba(255,255,255,0.85)" stroke-width="2" marker-end="url(#a3)"/></svg>
                </div>
                <div class="em-wave" style="top:75%; animation-delay:0.9s; animation-duration:1.6s;">
                    <svg width="180" height="26" viewBox="0 0 180 26"><defs><marker id="a4" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="rgba(255,255,255,0.9)"/></marker></defs><path d="M0,13 Q15,0 30,13 T60,13 T90,13 T120,13 T150,13" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="2" marker-end="url(#a4)"/></svg>
                </div>
                <div class="em-wave" style="top:22%; animation-delay:0.15s; animation-duration:1.2s;">
                    <svg width="140" height="22" viewBox="0 0 140 22"><defs><marker id="uv1" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="rgba(167,100,255,0.9)"/></marker></defs><path d="M0,11 Q10,0 20,11 T40,11 T60,11 T80,11 T100,11 T120,11" fill="none" stroke="rgba(167,100,255,0.85)" stroke-width="2" marker-end="url(#uv1)"/></svg>
                </div>
                <div class="em-wave" style="top:45%; animation-delay:0.5s; animation-duration:1.1s;">
                    <svg width="140" height="22" viewBox="0 0 140 22"><defs><marker id="uv2" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="rgba(167,100,255,0.9)"/></marker></defs><path d="M0,11 Q10,0 20,11 T40,11 T60,11 T80,11 T100,11 T120,11" fill="none" stroke="rgba(167,100,255,0.8)" stroke-width="2" marker-end="url(#uv2)"/></svg>
                </div>
                <div class="em-wave" style="top:68%; animation-delay:0.8s; animation-duration:1.3s;">
                    <svg width="140" height="22" viewBox="0 0 140 22"><defs><marker id="uv3" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="rgba(167,100,255,0.9)"/></marker></defs><path d="M0,11 Q10,0 20,11 T40,11 T60,11 T80,11 T100,11 T120,11" fill="none" stroke="rgba(167,100,255,0.85)" stroke-width="2" marker-end="url(#uv3)"/></svg>
                </div>
                <div class="tubes-container">
        """ + tubes_html + """
                </div>
            </div>
        </body></html>
        """
        components.html(anim_html, height=800)
        import time
        time.sleep(3.5)
        st.session_state.animating_radiation = False
        go_to(4)
        st.rerun()

    st.markdown("""
    <div class="content-card">
        <h2>☀️ Exposição à Luz Solar</h2>
        <p>
            Os tubos embrulhados são agora expostos à <strong>radiação solar direta</strong>.
            Insira o tempo de exposição para simular a passagem do tempo e os respetivos resultados.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if 'time_exp' not in st.session_state:
        st.session_state.time_exp = 30

    st.session_state.time_exp = st.number_input(
        "⏱️ Tempo de Exposição (minutos)",
        min_value=0, max_value=300, value=st.session_state.time_exp, step=1,
        help="Insira o número de minutos de exposição à luz solar. Tempos maiores levam a um maior escurecimento."
    )
    time_exp = st.session_state.time_exp

    # Sun animation bar
    sun_pct = min((time_exp / 60.0) * 100, 100) # cap at 100% for the gradient bar
    st.markdown(f"""
    <div style="
        max-width:700px; margin:0 auto 20px auto;
        background: linear-gradient(90deg, #FEF3C7 0%, #FDE68A {sun_pct}%, #E5E7EB {sun_pct}%, #E5E7EB 100%);
        border-radius: 20px; padding: 8px 16px;
        display:flex; align-items:center; justify-content:space-between;
        font-family:'Inter',sans-serif; font-size:14px; color:#92400E;
    ">
        <span>🌅 0 min</span>
        <span style="font-size:24px; filter:drop-shadow(0 0 6px rgba(251,191,36,0.6)); transition:all 0.3s;">
            {"🌞" if time_exp > 0 else "🌑"}
        </span>
        <span>60+ min ☀️</span>
    </div>
    """, unsafe_allow_html=True)

    components.html(render_tubes_html(TUBES, time_exp, show_wrapper=True, hide_result=True), height=310)

    if time_exp > 0:
        st.markdown(f"""
        <div class="info-card">
            <span class="icon">🔬</span>
            <strong>Tempo decorrido: {time_exp} minuto{"s" if time_exp != 1 else ""}.</strong>
            A luz solar está a incidir sobre os tubos. Os embrulhos impedem a observação do resultado
            — avança para a secção seguinte para remover os embrulhos e revelar o que aconteceu!
        </div>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Preparação", use_container_width=True):
            go_to(2)
            st.rerun()
    with col3:
        if st.button("Ver Resultados 🔍 →", use_container_width=True, type="primary"):
            st.session_state.animating_radiation = True
            st.rerun()

# ── Step 4 – Resultados ────────────────────────────────────────────────────
elif current == 4:
    time_exp = st.session_state.get('time_exp', 15)
    TUBE_INFO = {
        "A": {"label": "Tubo A", "desc": "Alumínio", "color": "#6B7280"},
        "B": {"label": "Tubo B", "desc": "Celofane Azul", "color": "#3B82F6"},
        "C": {"label": "Tubo C", "desc": "Celofane Vermelho", "color": "#EF4444"},
        "D": {"label": "Tubo D", "desc": "Celofane Verde", "color": "#22C55E"},
        "E": {"label": "Tubo E", "desc": "Sem embrulho", "color": "#F59E0B"},
    }
    CORRECT_ORDER = ["A", "C", "D", "B", "E"]

    if "order_seq" not in st.session_state:
        st.session_state.order_seq = []
    if "order_checked" not in st.session_state:
        st.session_state.order_checked = False
    if "order_correct" not in st.session_state:
        st.session_state.order_correct = False

    # ── Observe the tubes ──────────────────────────────────────────────────
    st.markdown(f"""
    <div class="content-card">
        <h2>🔍 Remoção dos Embrulhos e Observação</h2>
        <p>
            Após <strong>{time_exp} minutos</strong> de exposição à luz solar, removemos os embrulhos de todos os tubos.
            Observa o grau de <strong>escurecimento</strong> do precipitado em cada tubo:
        </p>
    </div>
    """, unsafe_allow_html=True)

    components.html(render_tubes_html(TUBES, time_exp, show_wrapper=False, animate_removal=True), height=350)

    st.divider()

    # ── Ordering challenge ────────────────────────────────────────────────
    st.markdown("""
    <div class="content-card">
        <h2>🧩 Desafio: Ordena os Tubos!</h2>
        <p>
            Com base no escurecimento observado, ordena os cinco tubos por
            <strong>ordem crescente da energia da luz incidente</strong> que cada um recebeu
            (do menos energético para o mais energético).
            Clica nas caixinhas pela ordem pretendida.
        </p>
    </div>
    """, unsafe_allow_html=True)

    selected = st.session_state.order_seq
    remaining = [t for t in TUBE_INFO if t not in selected]

    # Current sequence display
    if selected:
        st.markdown("<p style='font-weight:600; color:#4B5563; margin-bottom:8px;'>A tua ordenação (1.º = menos energético &nbsp;→&nbsp; último = mais energético):</p>", unsafe_allow_html=True)
        seq_html = '<div style="display:flex; gap:12px; flex-wrap:wrap; margin-bottom:16px; align-items:center;">'
        for i, tid in enumerate(selected):
            info = TUBE_INFO[tid]
            arrow = '<span style="font-size:22px; color:#9CA3AF; align-self:center;">→</span>' if i > 0 else ""
            seq_html += f"""
            {arrow}
            <div style="
                background:{info['color']}; color:white;
                border-radius:14px; padding:14px 20px; text-align:center;
                min-width:100px; box-shadow:0 4px 12px rgba(0,0,0,0.15);
                animation: fadeInUp 0.4s ease;
                font-family: 'Inter', sans-serif;
            ">
                <div style="font-size:20px; font-weight:800;">{info['label']}</div>
                <div style="font-size:12px; opacity:0.85; margin-top:4px;">{info['desc']}</div>
                <div style="font-size:11px; margin-top:6px; opacity:0.65;">#{i+1}</div>
            </div>
            """
        seq_html += """</div>
        <style>
          @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to   { opacity: 1; transform: translateY(0); }
          }
        </style>"""
        components.html(seq_html, height=130)

    # Available tube buttons
    if remaining and not st.session_state.order_correct:
        st.markdown("<p style='font-weight:600; color:#4B5563; margin:12px 0 8px 0;'>Clica num tubo para o adicionar à tua ordenação:</p>", unsafe_allow_html=True)
        btn_cols = st.columns(len(remaining))
        for col, tid in zip(btn_cols, remaining):
            info = TUBE_INFO[tid]
            with col:
                st.markdown(f"""
                <style>
                .tube-btn-{tid} button {{
                    background: {info['color']} !important;
                    color: white !important;
                    border: none !important;
                    border-radius: 14px !important;
                    font-weight: 700 !important;
                    font-size: 14px !important;
                    padding: 14px 10px !important;
                    width: 100% !important;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
                    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
                }}
                .tube-btn-{tid} button:hover {{
                    transform: translateY(-3px) !important;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.2) !important;
                }}
                </style>
                """, unsafe_allow_html=True)
                st.markdown(f'<div class="tube-btn-{tid}">', unsafe_allow_html=True)
                if st.button(f"{info['label']}\n{info['desc']}", key=f"order_pick_{tid}", use_container_width=True):
                    st.session_state.order_seq.append(tid)
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

    # Check / Reset
    if not st.session_state.order_correct:
        action_cols = st.columns([1, 1, 4])
        with action_cols[0]:
            if selected:
                if st.button("🗑️ Recomeçar", key="order_reset", use_container_width=True):
                    st.session_state.order_seq = []
                    st.session_state.order_checked = False
                    st.rerun()
        with action_cols[1]:
            if len(selected) == 5:
                if st.button("✅ Verificar", key="order_check", use_container_width=True, type="primary"):
                    st.session_state.order_checked = True
                    if selected == CORRECT_ORDER:
                        st.session_state.order_correct = True
                    st.rerun()

        if st.session_state.order_checked and not st.session_state.order_correct:
            wrong_count = sum(1 for i in range(5) if selected[i] != CORRECT_ORDER[i])
            st.error(f"❌ Não está correto — tens {5 - wrong_count} posição(ões) certa(s). Tenta novamente!")

    # ── Conclusions — only revealed after correct ordering ─────────────────
    if st.session_state.order_correct:
        st.success("🎉 **Perfeito!** Ordenaste corretamente os tubos. Vê as conclusões abaixo.")
        st.markdown("""
        <div class="content-card" style="margin-top:24px;">
            <h2>📋 Conclusões</h2>
            <p style="margin-bottom:20px;">
                A energia da luz incidente afeta diretamente a extensão da reação fotoquímica.
                Quanto <strong>maior a frequência</strong> (e portanto a energia) dos fotões,
                mais extensa é a decomposição do AgCl:
            </p>
        </div>
        """, unsafe_allow_html=True)

        conclusions = [
            ("A", "#6B7280", "Alumínio (controlo)", "Sem escurecimento.",
             "O alumínio é opaco — bloqueia toda a radiação. Serve como ensaio de controlo, provando que sem luz a reação não ocorre.", "#F3F4F6"),
            ("C", "#EF4444", "Celofane Vermelho", "Escurecimento ligeiro.",
             "A luz vermelha é a menos energética do espetro visível (menor frequência), provocando uma decomposição muito limitada.", "#FEF2F2"),
            ("D", "#22C55E", "Celofane Verde", "Escurecimento intermédio.",
             "A luz verde possui energia intermédia — fotões com frequência superior à vermelha, causando maior decomposição.", "#F0FDF4"),
            ("B", "#3B82F6", "Celofane Azul", "Escurecimento acentuado.",
             "A luz azul é a mais energética dos filtros testados (maior frequência), promovendo uma decomposição significativa.", "#EFF6FF"),
            ("E", "#F59E0B", "Sem embrulho", "Escurecimento máximo.",
             "Recebe todo o espetro visível e UV. A combinação de todas as frequências produz a maior extensão da reação.", "#FFFBEB"),
        ]
        for label, color, title, result, explanation, bg in conclusions:
            st.markdown(f"""
            <div class="conclusion-item" style="background:{bg};">
                <div class="tube-badge" style="background:{color};">{label}</div>
                <div class="text">
                    <strong>{title}</strong> — {result}
                    <p>{explanation}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="equation-card" style="margin-top:20px; background:linear-gradient(135deg, #FEF3C7, #FDE68A); border-color:#F59E0B;">
            <div style="font-size:0.85em; color:#92400E; margin-bottom:8px; font-weight:600;">Ordenação por energia crescente da luz incidente</div>
            <span style="color:#78350F; font-size:1.1em;">
                A (nenhuma) &lt; C (vermelha) &lt; D (verde) &lt; B (azul) &lt; E (luz branca completa)
            </span>
        </div>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Exposição", use_container_width=True):
            go_to(3)
            st.rerun()
    with col3:
        # Only allow advancing once ordering is correct
        if st.session_state.order_correct:
            if st.button("Questões 📝 →", use_container_width=True, type="primary"):
                go_to(5)
                st.rerun()
        else:
            st.button("Questões 📝 →", use_container_width=True, type="primary", disabled=True, help="Ordena corretamente os tubos para avançar.")


# ── Step 5 – Questões ──────────────────────────────────────────────────────
elif current == 5:
    st.markdown("""
    <div class="content-card">
        <h2>📝 Testa os Teus Conhecimentos</h2>
        <p>Responde às seguintes questões para consolidares a aprendizagem.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Pré-laboratoriais ──
    st.markdown("### 🔬 Questões Pré-Laboratoriais")

    st.markdown('<div class="question-card"><h3>Questão 1</h3>', unsafe_allow_html=True)
    st.markdown("""
    A preparação do cloreto de prata envolve a mistura de duas soluções:
    - **Solução A:** Transparente incolor. Inofensiva.
    - **Solução B:** Transparente incolor. Provoca manchas escuras na pele e, se for concentrada, é corrosiva.

    *Qual das soluções é de cloreto de sódio? E qual é de nitrato de prata?*
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    q1 = st.radio("Selecione:", [
        "A é Cloreto de Sódio (NaCl) · B é Nitrato de Prata (AgNO₃)",
        "A é Nitrato de Prata (AgNO₃) · B é Cloreto de Sódio (NaCl)",
    ], index=None, key="q1", label_visibility="collapsed")
    if q1:
        if "A é Cloreto de Sódio" in q1:
            st.success("✅ Correto! O NaCl (sal de cozinha) é inofensivo. O AgNO₃ provoca manchas escuras na pele devido à fotossensibilidade dos iões prata.")
        else:
            st.error("❌ Tenta novamente. Pensa: qual é o sal que usamos na cozinha?")

    st.markdown("")

    st.markdown('<div class="question-card"><h3>Questão 2</h3>', unsafe_allow_html=True)
    st.markdown("""
    Um papel de revestimento dos tubos de ensaio deve ser opaco. Os outros devem ser **____**.
    Apesar de Cl₂ ser um gás tóxico, a reação pode ser realizada sem receio, desde que em pequena escala,
    porque, nessas condições, o gás libertado **____**.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    q2 = st.radio("Selecione:", [
        "(A) opacos de cores diferentes · não é tóxico",
        "(B) opacos de cores diferentes · é em quantidade diminuta",
        "(C) transparentes de cores diferentes · não é tóxico",
        "(D) transparentes de cores diferentes · é em quantidade diminuta",
    ], index=None, key="q2", label_visibility="collapsed")
    if q2:
        if "(D)" in q2:
            st.success("✅ Correto! Os celofanes são transparentes e coloridos para filtrar cores específicas. A escala reduzida garante que a quantidade de Cl₂ libertada é ínfima e segura.")
        else:
            st.error("❌ Não é essa. Os celofanes precisam de ser transparentes para deixar passar luz!")

    # ── Pós-laboratoriais ────────────────────────────────────────────────────
    st.markdown("")
    st.markdown("### 📊 Questões Pós-Laboratoriais")

    # ── Restantes questões pós-laboratoriais ─────────────────────────────────
    questions = [
        ("Questão 3", "Justifique que um dos tubos não tenha sido embrulhado e que um deles tenha sido revestido com papel de alumínio.",
         "O tubo **E** (sem embrulho) permite receber todo o espetro de luz, servindo de referência para o efeito máximo. O tubo **A** (alumínio) funciona como **ensaio de controlo** (em branco), demonstrando que, na ausência de radiação, a reação fotoquímica não ocorre."),

        ("Questão 4", "Justifique o procedimento 2 e, no procedimento 6, terem-se desembrulhado os tubos de ensaio todos ao mesmo tempo.",
         "No **procedimento 2**, embrulham-se os tubos *antes* de os expor à luz para garantir que o AgCl só recebe radiação filtrada. Desembrulham-se **todos ao mesmo tempo** para que a observação seja feita em condições iguais, evitando que alguns tubos fiquem mais tempo expostos à luz após a remoção do embrulho."),

        ("Questão 5", "Qual é a cor da luz incidente com energia mínima para a qual se observou escurecimento do AgCl?",
         "**Vermelha** (tubo C). Embora o escurecimento seja muito ténue, a luz vermelha (a de menor frequência/energia no visível entre as testadas) é suficiente para promover alguma decomposição fotoquímica do AgCl."),

        ("Questão 6", "Preveja, justificando, se observaria escurecimento caso fosse utilizado um papel celofane **violeta**.",
         "**Sim**, observar-se-ia escurecimento, provavelmente **mais acentuado** do que com o celofane azul. A luz violeta tem **maior frequência** do que a azul, logo os seus fotões transportam **maior energia** (E = h·f), promovendo a reação fotoquímica de forma mais eficaz."),
    ]

    for title, question, answer in questions:
        st.markdown(f'<div class="question-card"><h3>{title}</h3><p>{question}</p></div>', unsafe_allow_html=True)
        if st.button(f"💡 Ver Resposta — {title}", key=f"btn_{title}"):
            st.info(answer)
        st.markdown("")

    st.markdown("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Resultados", use_container_width=True):
            go_to(4)
            st.rerun()
    with col2:
        if st.button("🔄 Recomeçar a Atividade", use_container_width=True, type="secondary"):
            go_to(0)
            st.rerun()
