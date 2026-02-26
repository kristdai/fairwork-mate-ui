import streamlit as st
import time

# ─── Page Config ───
st.set_page_config(
    page_title="FairWork Mate",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Replace with your Google Drive logo direct link ───
LOGO_URL = "https://github.com/kristdai/fairwork-mate-ui/blob/main/Screenshot%202026-02-26%20112050.png"

# ─── Custom CSS ───
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

/* ── hide streamlit chrome ── */
#MainMenu, footer, header {visibility:hidden;}
.block-container {padding-top:1.5rem;padding-bottom:2rem;max-width:820px;}
.stApp {background:#fff;font-family:'Inter',sans-serif;}

/* ── brand bar ── */
.brand{display:flex;align-items:center;gap:10px;padding:4px 0 24px 0;}
.brand img{width:46px;height:46px;border-radius:10px;}
.brand span{font-size:1.45rem;font-weight:700;color:#4A1D8E;}

/* ── hero ── */
.hero-title{text-align:center;font-size:3.2rem;font-weight:900;color:#111;margin:18px 0 4px;line-height:1.12;}
.hero-title .accent{color:#7C3AED;}
.hero-sub{text-align:center;color:#555;font-size:1rem;line-height:1.75;max-width:590px;margin:10px auto 36px;}

/* ── tall text area (3x height) ── */
div[data-testid="stTextArea"] textarea{
    border:2px solid #E9D5FF!important;border-radius:14px!important;
    padding:16px 18px!important;font-size:.95rem!important;
    font-family:'Inter',sans-serif!important;background:#fff!important;
    min-height:126px!important;height:126px!important;
    resize:none!important;
}
div[data-testid="stTextArea"] textarea:focus{
    border-color:#7C3AED!important;box-shadow:0 0 0 2px rgba(124,58,237,.15)!important;
}

/* ── regular text input (chat page) ── */
div[data-testid="stTextInput"] input{
    border:2px solid #E9D5FF!important;border-radius:12px!important;
    padding:14px 16px!important;font-size:.95rem!important;
    font-family:'Inter',sans-serif!important;background:#fff!important;
}
div[data-testid="stTextInput"] input:focus{
    border-color:#7C3AED!important;box-shadow:0 0 0 2px rgba(124,58,237,.15)!important;
}

/* ── primary button ── */
.stButton>button{
    background:#7C3AED!important;color:#fff!important;border:none!important;
    border-radius:14px!important;padding:.7rem 1.6rem!important;
    font-size:1rem!important;font-weight:600!important;
    font-family:'Inter',sans-serif!important;transition:.2s;
}
.stButton>button:hover{background:#6D28D9!important;color:#fff!important;}
.stButton>button:active{background:#5B21B6!important;}

/* back button override */
.back-btn button{
    background:transparent!important;color:#7C3AED!important;
    border:2px solid #E9D5FF!important;
}
.back-btn button:hover{background:#FAF5FF!important;border-color:#7C3AED!important;}

/* ── footer ── */
.footer{text-align:center;color:#999;font-size:.82rem;margin-top:42px;letter-spacing:.01em;}

/* ── chat bubbles ── */
.chat-user{
    background:#F3E8FF;color:#1a1a1a;
    padding:14px 20px;border-radius:18px 18px 4px 18px;
    margin:6px 0 6px auto;max-width:72%;width:fit-content;
    font-size:.95rem;line-height:1.55;
}
.chat-bot-wrap{
    background:#F9FAFB;border:1px solid #E5E7EB;
    padding:18px 22px;border-radius:18px 18px 18px 4px;
    margin:6px auto 6px 0;max-width:88%;
    font-size:.95rem;line-height:1.7;color:#1a1a1a;
}
.chat-bot-wrap strong,.chat-bot-wrap b{color:#7C3AED;}
.source-line{margin-top:14px;padding-top:10px;border-top:1px solid #E5E7EB;font-size:.82rem;color:#999;}

/* ── divider ── */
.sep{border:none;border-top:1px solid #f0f0f0;margin:18px 0;}
</style>
""",
    unsafe_allow_html=True,
)

# ─── Session State ───
if "messages" not in st.session_state:
    st.session_state.messages = []
if "page" not in st.session_state:
    st.session_state.page = "home"

# ─── Dummy Responses ───
RESPONSES = {
    "default": """Based on the **General Retail Industry Award 2020** (MA000004), here is the breakdown:

**Sunday Penalty Rate — Casual Level 2 Retail Employee:**

| Component | Detail |
|---|---|
| Base hourly rate (Level 2) | **$25.52 /hr** |
| Casual loading | 25 % |
| Sunday penalty (casual) | **200 %** of base rate |
| **Total Sunday casual rate** | **$63.80 /hr** |

**Key points:**
- The Sunday rate for a *casual* employee under this award is **200 %** of the ordinary hourly rate (inclusive of casual loading).
- Effective from the **1 July 2024** pay period.
- Applies to **all ordinary hours** worked on a Sunday.

📋 **Source:** *General Retail Industry Award 2020*, Clause 26.2 — Penalty rates, Table 9 — Fair Work Commission.

⚠️ *This is AI-generated guidance. Always verify with the official Fair Work Commission documentation or seek professional advice.*""",
    "sick": """Under the **National Employment Standards (NES)** — *Fair Work Act 2009*:

**Personal / Carer's Leave entitlements:**

| Employee type | Paid leave per year | Unpaid carer's leave |
|---|---|---|
| Full-time | **10 days** | 2 days / occasion |
| Part-time | **10 days** (pro-rata) | 2 days / occasion |
| Casual | ✗ Not entitled | 2 days / occasion |

**Important rules:**
- Paid personal leave **accumulates** from year to year with no cap.
- Employer may request a **medical certificate** or statutory declaration for absences ≥ 1 day.
- Some modern awards require evidence for absences directly **before or after** a public holiday or weekend.

📋 **Source:** *Fair Work Act 2009*, Part 2-2, Division 7 — Personal/carer's leave & compassionate leave.

⚠️ *AI-generated guidance — verify with the Fair Work Commission.*""",
    "overtime": """Under the **General Retail Industry Award 2020** (MA000004):

**Overtime rates — Full-time & Part-time employees:**

| Period | Rate |
|---|---|
| First 3 hrs of overtime | **150 %** (time-and-a-half) |
| After 3 hrs of overtime | **200 %** (double time) |
| Sunday overtime | **200 %** |
| Public holiday overtime | **250 %** |

**When does overtime start?**
- Full-time: after **38 ordinary hours** per week or outside the spread of ordinary hours.
- Part-time: after **agreed hours** per week (or 38 hours — whichever is lower).
- Casual: after **38 hours** per week. Overtime rate replaces the casual loading.

📋 **Source:** *General Retail Industry Award 2020*, Clause 28 — Overtime. Fair Work Commission.

⚠️ *AI-generated guidance — verify with official documentation.*""",
    "notice": """Under the **National Employment Standards** and most modern awards:

**Minimum notice periods (employer-initiated termination):**

| Period of continuous service | Minimum notice |
|---|---|
| ≤ 1 year | **1 week** |
| 1 – 3 years | **2 weeks** |
| 3 – 5 years | **3 weeks** |
| 5 + years | **4 weeks** |

> Employees **over 45 years old** with at least 2 years of service get an **additional week**.

**Redundancy pay** is separate and ranges from **4 weeks'** pay (1–2 yrs) up to **16 weeks'** pay (9–10 yrs). Small businesses (< 15 employees) are exempt from redundancy pay requirements.

📋 **Source:** *Fair Work Act 2009*, s.117 (Notice of termination) & s.119 (Redundancy pay).

⚠️ *AI-generated guidance — verify with the Fair Work Commission.*""",
}


def get_response(q: str) -> str:
    ql = q.lower()
    if any(k in ql for k in ["sick", "personal leave", "carer"]):
        return RESPONSES["sick"]
    if any(k in ql for k in ["overtime", "extra hours", "time and a half"]):
        return RESPONSES["overtime"]
    if any(k in ql for k in ["notice", "termination", "redundancy", "fired", "sacked"]):
        return RESPONSES["notice"]
    return RESPONSES["default"]


# ─── Brand Header ───
st.markdown(
    f"""
<div class="brand">
    <img src="{LOGO_URL}" alt="logo" onerror="this.style.background='#7C3AED';this.style.display='block';this.alt='FM';">
    <span>fairwork.mate</span>
</div>
""",
    unsafe_allow_html=True,
)

# ════════════════════════════════════════════
#  HOME PAGE
# ════════════════════════════════════════════
if st.session_state.page == "home":

    st.markdown(
        """
    <div class="hero-title">Stop Assuming. <span class="accent">Start Asking.</span></div>
    <div class="hero-sub">
        Australian Employment Law is complex. Your answers shouldn't be.
        Instantly decode 120+ Modern Awards with an AI that cites its sources.
        No hallucinations, just compliance.
    </div>
    """,
        unsafe_allow_html=True,
    )

    # ── Tall text area input (no card/hint above) ──
    question = st.text_area(
        "question",
        placeholder="What is the Sunday penalty rate for a casual Level 2 retail employee?",
        label_visibility="collapsed",
        height=126,
        key="home_q",
    )

    _, rc = st.columns([3, 2])
    with rc:
        go = st.button("✨ Ask FairWork Mate", key="home_btn", use_container_width=True)

    if go:
        q = (
            question.strip()
            if question.strip()
            else "What is the Sunday penalty rate for a casual Level 2 retail employee?"
        )
        st.session_state.messages.append({"role": "user", "content": q})
        st.session_state.messages.append(
            {"role": "assistant", "content": get_response(q)}
        )
        st.session_state.page = "chat"
        st.rerun()

    # ── sample questions ──
    st.markdown("<br>", unsafe_allow_html=True)
    sample_cols = st.columns(3)
    samples = [
        "💊 How much sick leave am I entitled to?",
        "⏱️ When do overtime rates kick in for retail?",
        "📝 What notice period must my employer give?",
    ]
    for col, s in zip(sample_cols, samples):
        with col:
            if st.button(s, key=f"sample_{s}", use_container_width=True):
                clean = s.split(" ", 1)[1]
                st.session_state.messages.append({"role": "user", "content": clean})
                st.session_state.messages.append(
                    {"role": "assistant", "content": get_response(clean)}
                )
                st.session_state.page = "chat"
                st.rerun()

    st.markdown(
        '<div class="footer">🔒 Powered by Azure AI · citing Fair Work Commission Documents · 24/7 Availability</div>',
        unsafe_allow_html=True,
    )

# ════════════════════════════════════════════
#  CHAT PAGE
# ════════════════════════════════════════════
elif st.session_state.page == "chat":

    left, right = st.columns([1, 3])
    with left:
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("← New Chat", key="back"):
            st.session_state.messages = []
            st.session_state.page = "home"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<hr class="sep">', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f'<div class="chat-user">{msg["content"]}</div>',
                unsafe_allow_html=True,
            )
        else:
            with st.container():
                st.markdown(msg["content"])

    st.markdown('<hr class="sep">', unsafe_allow_html=True)

    st.markdown(
        '<p style="font-size:.85rem;color:#888;margin-bottom:4px;">Ask a follow-up question</p>',
        unsafe_allow_html=True,
    )

    follow_up = st.text_input(
        "follow-up",
        placeholder="e.g. What about public holiday rates?",
        label_visibility="collapsed",
        key="chat_q",
    )

    _, rc2 = st.columns([3, 2])
    with rc2:
        send = st.button(
            "✨ Ask FairWork Mate", key="chat_btn", use_container_width=True
        )

    if send and follow_up.strip():
        st.session_state.messages.append({"role": "user", "content": follow_up.strip()})
        st.session_state.messages.append(
            {"role": "assistant", "content": get_response(follow_up)}
        )
        st.rerun()

    st.markdown(
        '<div class="footer">🔒 Powered by Azure AI · citing Fair Work Commission Documents · 24/7 Availability</div>',
        unsafe_allow_html=True,
    )
