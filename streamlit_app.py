import streamlit as st
from detect import detect
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title='BE Project', page_icon=':guardsman:', layout='wide')

# Define function to display video frames
def show_frame(image):
    # Resize image to fit in designated box
    # image = cv2.resize(image, (640, 480))
    # Display image
    st.image(image, channels='BGR')

# Create UI components
st.title('BE Project')

# Add avatars to title
avatars = ['🚀', '🧑‍🚀', '👩‍🚀', '🌌', '🪐']
avatar = st.selectbox('', options=avatars, index=0, key='avatar')


st.image(f'https://avatars.dicebear.com/api/avataaars/{avatar}.svg', width=50)

st.write('Enter a video file path or HTTP link below:')

# Add design to input field
st.markdown("""<style>
                .stTextInput>div>div>div>input {
                    border: 2px solid #7c7c7c;
                    border-radius: 25px;
                    padding: 10px;
                    font-size: 18px;
                    background-color: #f2f2f2;
                }
                </style>""", unsafe_allow_html=True)

input_type = st.radio('', ['Video', 'HTTP link'])
input_value = st.text_input('', '')

# If input is a video file
if input_type == 'Video':
    pass
    
elif input_type == 'HTTP link':
    # Open URL and read image data
    link=input_value
    if(link==""):
        detect(source="http://192.168.1.9:4747/video")
    else:
        detect(source=link)
    # show_frame(image)

# Add design to output area
st.markdown("""<style>
                .streamlit-expanderHeader {
                    background-color: #7c7c7c !important;
                    color: white !important;
                    font-size: 20px !important;
                }
                .streamlit-expanderContent {
                    background-color: #f2f2f2 !important;
                    padding: 10px !important;
                }
                </style>""", unsafe_allow_html=True)

# Add external design library
components.html("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss/dist/tailwind.min.css">
    <style>
        .btn {
            padding: 10px 30px;
            border-radius: 25px;
            font-weight: bold;
            background-color: #7c7c7c;
            color: white;
            transition: all 0.2s ease-in-out;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0px 2px 5px #7c7c7c;
            cursor: pointer;
        }
    </style>
""", height=0)

# # Add button with external design
# if st.button('Detect', key='detect'):
#     components.html('<div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">Detection successful!</div>')
