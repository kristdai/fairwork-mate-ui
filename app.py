import streamlit as st

# ---------------------------
# Page config + basic CSS
# ---------------------------
st.set_page_config(page_title="fairwork.mate", page_icon="💬", layout="centered")

st.markdown(
    """
    <style>
      :root{
        --purple:#6C3EF2;
        --purple-dark:#5A2FE0;
        --text:#111111;
        --muted:#6B7280;
        --card:#F2ECFF;
        --border:#E5E7EB;
      }
      /* tighten default Streamlit padding */
      .block-container { padding-top: 2.2rem; padding-bottom: 2.0rem; max-width: 980px; }
      /* remove extra top spacing */
      header { visibility: hidden; height: 0px; }

      /* brand row */
      .brand-row{
        display:flex; align-items:center; gap:14px; margin-bottom: 10px;
      }
      .brand-badge{
        width:44px; height:44px; border-radius:14px;
        background: radial-gradient(circle at 30% 30%, #B794F6, var(--purple));
        display:flex; align-items:center; justify-content:center;
        color:white; font-size:22px; font-weight:700;
        box-shadow: 0 8px 24px rgba(108,62,242,0.25);
      }
      .brand-name{
        font-size: 30px; font-weight: 800; letter-spacing: -0.02em;
      }

      /* hero */
      .hero-title{
        font-size: 62px; line-height: 1.02; font-weight: 900; letter-spacing: -0.03em;
        margin: 18px 0 10px 0;
      }
      .hero-title .accent{ color: var(--purple); }
      .hero-sub{
        font-size: 18px; line-height: 1.45; color: var(--muted);
        max-width: 860px; margin: 0 auto 20px auto;
      }

      /* CTA button styling (Streamlit uses <button> inside .stButton) */
      div.stButton > button{
        background: var(--purple);
        border: 1px solid rgba(0,0,0,0.06);
        color: white;
        padding: 12px 22px;
        border-radius: 14px;
        font-weight: 800;
        font-size: 18px;
        box-shadow: 0 10px 24px rgba(108,62,242,0.25);
      }
      div.stButton > button:hover{
        background: var(--purple-dark);
        border-color: rgba(0,0,0,0.08);
      }

      /* helper line */
      .helper{
        display:flex; gap:14px; align-items:center; justify-content:center;
        color: var(--muted);
        font-size: 14px;
        margin-top: 10px;
      }
      .helper .dot{ opacity: 0.5; }

      /* example card */
      .example-card{
        margin-top: 26px;
        background: var(--card);
        border: 1px solid rgba(108,62,242,0.12);
        border-radius: 18px;
        padding: 18px 18px 14px 18px;
      }
      .example-row{
        display:flex; align-items:center; justify-content:space-between; gap:14px;
        flex-wrap: wrap;
      }
      .example-q{
        font-size: 20px;
        color: var(--text);
        font-weight: 600;
      }
      .example-q b{ font-weight: 900; }
      .example-q .accent{ color: var(--purple); font-weight: 900; }
      .example-cta{
        display:flex; align-items:center; justify-content:flex-end;
        margin-top: 10px;
      }
      /* make the second button smaller */
      .small-cta div.stButton > button{
        font-size: 16px !important;
        padding: 10px 16px !important;
        border-radius: 14px !important;
        box-shadow: none !important;
      }

      /* center text blocks */
      .center { text-align: center; }

      /* input look */
      .stTextInput input{
        border-radius: 12px;
        border: 1px solid var(--border);
        padding: 12px 12px;
      }

      /* chat container */
      .chat-wrap{
        margin-top: 16px;
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 14px 14px;
        background: white;
      }

    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Session state
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []  # [{"role": "user"/"assistant", "content": "..."}]

# ---------------------------
# Header / Hero
# ---------------------------
st.markdown(
    """
    <div class="brand-row">
      <div class="brand-badge">👎</div>
      <div class="brand-name">fairwork.mate</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="center">
      <div class="hero-title">Stop Assuming. <span class="accent">Start Asking.</span></div>
      <div class="hero-sub">
        Australian Employment Law is complex. Your answers shouldn't be.
        Instantly decode 120+ Modern Awards with an AI that cites its sources.
        No hallucinations, just compliance.
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Primary CTA (UI-only)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    if st.button("✨ Ask FairWork Mate", use_container_width=True):
        st.session_state.show_chat = True

st.markdown(
    """
    <div class="helper">
      <span>🔒 Powered by Azure AI</span><span class="dot">•</span>
      <span>citing Fair Work Commission Documents</span><span class="dot">•</span>
      <span>24/7 Availability</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Example card with pre-filled prompt
# ---------------------------
st.markdown(
    """
    <div class="example-card">
      <div class="example-row">
        <div class="example-q">
          What is the Sunday <b>penalty rate</b> for a casual <span class="accent">Level 2</span> retail employee?
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    ex_cols = st.columns([3, 1])
    with ex_cols[0]:
        example_clicked = st.text_input(
            label="",
            placeholder="Type your question here…",
            key="q_input",
            label_visibility="collapsed",
        )
    with ex_cols[1]:
        st.markdown('<div class="small-cta">', unsafe_allow_html=True)
        ask_clicked = st.button("✨ Ask FairWork Mate", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# Chat UI (UI-only placeholder behaviour)
# ---------------------------
show_chat = st.session_state.get("show_chat", True)

if show_chat:
    st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)

    # Render messages
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    # If example ask clicked, treat input as user message
    if ask_clicked and (example_clicked or st.session_state.get("q_input", "").strip()):
        user_text = (example_clicked or st.session_state.get("q_input", "")).strip()
        if user_text:
            st.session_state.messages.append({"role": "user", "content": user_text})
            # UI-only simulated assistant response (loading)
            with st.chat_message("assistant"):
                with st.spinner("Thinking…"):
                    st.write("")

    # Standard chat input
    prompt = st.chat_input("Ask a question about awards, pay rates, leave, or compliance…")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                st.write("")

    st.markdown("</div>", unsafe_allow_html=True)
