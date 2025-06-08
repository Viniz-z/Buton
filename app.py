import warnings
warnings.filterwarnings("ignore")
import streamlit as st
# HTML + CSS do botão
botao_html = """
<style>
.button {
  cursor: pointer;
  display: flex;
  text-wrap: nowrap;
  align-items: center;
  gap: 0.9rem;
  padding: 1.5rem 2rem;
  border-radius: 1.2rem;
  background: linear-gradient(to bottom, #e3a8fc, #8d38cf);
  box-sizing: border-box;
  box-shadow: -3px 5px 1.5px #5a2982, -15px 12px 20px #5a2982ba;
  border: none;
  transform: rotate3d(2, -1, 1, 343deg) rotatex(27deg) scale(0.9);
  color: #ffcaf7;
  font-weight: bold;
  font-size: 1.2rem;
  transition: all 0.2s;
  position: relative;
}
.button:before {
  content: "";
  width: 97%;
  position: absolute;
  height: 91%;
  top: 4.5%;
  z-index: -2;
  left: 1.3%;
  border-radius: 1.1rem;
  box-shadow: inset 0 -5px 5px -1px #7926bc;
  background: linear-gradient(to bottom, #d591ff, #7f2dc2);
}
.button:hover {
  transform: scale(1.2);
  box-shadow: inset -0.5px -3px 3px 1px #7926bc;
}
.button:active {
  transform: scale(1.15);
  box-shadow: inset 2px 2px 3px #5a2982ba;
}
.icon {
  width: 1.8rem;
  height: 1.8rem;
}
.button span {
  background: -webkit-linear-gradient(#ffe4fe, #ffcaf7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.center {
  display: flex;
  justify-content: center;
  margin-top: 100px;
}
</style>

<div class="center">
  <form action="?join=true" method="post">
    <button class="button" type="submit">
      <span>Join Today</span>
      <svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none"
        viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3" />
      </svg>
    </button>
  </form>
</div>
"""

st.markdown(botao_html, unsafe_allow_html=True)

query_params = st.query_params
if "join" in query_params:
    st.success("Você clicou em 'Join Today' 🎉")
