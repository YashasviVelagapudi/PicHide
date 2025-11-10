import streamlit as st # type: ignore
from PIL import Image
import numpy as np
import io

st.title("🖼️ PicHide - Image in Image Steganography")
st.write("Hide one image inside another securely using LSB Steganography.")

mode = st.radio("Choose Mode:", ["Hide Image", "Reveal Image"])

# --- Hide Image Mode ---
if mode == "Hide Image":
    cover_file = st.file_uploader("Upload Cover Image", type=["png", "jpg", "jpeg"])
    secret_file = st.file_uploader("Upload Secret Image", type=["png", "jpg", "jpeg"])

    if cover_file and secret_file:
        cover = Image.open(cover_file).convert("RGB")
        secret = Image.open(secret_file).convert("RGB").resize(cover.size)

        cover_arr = np.array(cover)
        secret_arr = np.array(secret)

        # Hide 4 MSB of secret image inside 4 LSB of cover image
        encoded_arr = (cover_arr & 0xF0) | (secret_arr >> 4)
        encoded_img = Image.fromarray(encoded_arr.astype('uint8'), 'RGB')

        st.image(encoded_img, caption="✅ Encoded Image Preview", use_container_width=True)

        buf = io.BytesIO()
        encoded_img.save(buf, format="PNG")
        st.download_button("💾 Download Encoded Image", buf.getvalue(), file_name="encoded.png", mime="image/png")

# --- Reveal Image Mode ---
elif mode == "Reveal Image":
    encoded_file = st.file_uploader("Upload Encoded Image", type=["png", "jpg", "jpeg"])

    if encoded_file:
        encoded = Image.open(encoded_file).convert("RGB")
        encoded_arr = np.array(encoded)

        # Extract the hidden image
        secret_arr = (encoded_arr & 0x0F) << 4
        secret_img = Image.fromarray(secret_arr.astype('uint8'), 'RGB')

        st.image(secret_img, caption="🕵️ Hidden Image Revealed", use_container_width=True)

        buf = io.BytesIO()
        secret_img.save(buf, format="PNG")
        st.download_button("💾 Download Hidden Image", buf.getvalue(), file_name="decoded.png", mime="image/png")
