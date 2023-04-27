import streamlit as st
from detect import detect

st.set_page_config(page_title='BE Project')


# Define function to display video frames
def show_frame(image):
    # Resize image to fit in designated box
    # image = cv2.resize(image, (640, 480))
    # Display image
    st.image(image, channels='BGR')

# Create UI components
st.title('BE Project')
st.write('Enter a video file path or HTTP link below:')
input_type = st.radio('', ['Video', 'HTTP link'])
input_value = st.text_input('', '')

# If input is a video file
if input_type == 'Video':
    pass
    
elif input_type == 'HTTP link':
    # Open URL and read image data
    
    detect(source="http://192.168.1.9:4747/video")
    # show_frame(image)
