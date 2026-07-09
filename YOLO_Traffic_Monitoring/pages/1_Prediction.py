import streamlit as st
import cv2
import tempfile
import os

from detection.detector import detect_vehicles, detect_video


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Vehicle Detection",
    page_icon="🚗",
    layout="wide"
)


# ------------------------------------------------
# TITLE
# ------------------------------------------------

st.title("🚗 YOLO Vehicle Detection & Counting")

st.write(
    "Choose whether you want to detect vehicles from an image or a video."
)


option = st.radio(
    "Select Input Type",
    ["Image", "Video"]
)


# =====================================================
# IMAGE DETECTION
# =====================================================

if option == "Image":

    uploaded_image = st.file_uploader(
        "Upload Traffic Image",
        type=["jpg", "jpeg", "png"]
    )


    if uploaded_image is not None:

        with st.spinner("Detecting vehicles..."):

            temp_image = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".jpg"
            )

            temp_image.write(
                uploaded_image.read()
            )

            temp_image.close()


            detected_image, counts = detect_vehicles(
                temp_image.name
            )


        st.success("✅ Image processed successfully!")


        detected_image_rgb = cv2.cvtColor(
            detected_image,
            cv2.COLOR_BGR2RGB
        )


        st.subheader("📷 Detected Image")


        st.image(
            detected_image_rgb,
            use_container_width=True
        )


        st.subheader("🚘 Vehicle Count")


        total = sum(counts.values())


        st.metric(
            "Total Vehicles Detected",
            total
        )


        if counts:

            st.table(
                {
                    "Vehicle": list(counts.keys()),
                    "Count": list(counts.values())
                }
            )

        else:

            st.warning(
                "No vehicles detected."
            )


        # Download image

        result_image = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        )


        cv2.imwrite(
            result_image.name,
            detected_image
        )


        with open(
            result_image.name,
            "rb"
        ) as file:


            st.download_button(
                label="📥 Download Detected Image",
                data=file,
                file_name="detected_image.jpg",
                mime="image/jpeg"
            )



# =====================================================
# VIDEO DETECTION
# =====================================================


else:


    uploaded_video = st.file_uploader(
        "Upload Traffic Video",
        type=["mp4", "avi", "mov"]
    )


    if uploaded_video is not None:


        input_video = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        )


        input_video.write(
            uploaded_video.read()
        )


        input_video.close()



        output_video = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        )


        # Processing message container

        status = st.empty()


        try:

            status.info(
                "⏳ Processing video... Please wait."
            )


            result_video, counts = detect_video(
                input_video.name,
                output_video.name
            )


            status.empty()


            if os.path.exists(result_video):

                st.success(
                    "✅ Video processed successfully!"
                )


                st.subheader(
                    "🎥 Processed Video"
                )


                st.video(
                    result_video
                )


            else:

                st.error(
                    "❌ Output video was not created."
                )



        except Exception as e:

            status.empty()

            st.error(
                f"Video processing failed: {e}"
            )



        # Vehicle Count

        if 'counts' in locals():


            st.subheader(
                "🚘 Vehicle Count"
            )


            total = sum(
                counts.values()
            )


            st.metric(
                "Total Vehicles Detected",
                total
            )


            if counts:


                st.table(
                    {
                        "Vehicle": list(counts.keys()),
                        "Count": list(counts.values())
                    }
                )


            else:

                st.warning(
                    "No vehicles detected."
                )



        # Download button

        if os.path.exists(result_video):

            with open(
                result_video,
                "rb"
            ) as file:


                st.download_button(
                    label="📥 Download Processed Video",
                    data=file,
                    file_name="detected_video.mp4",
                    mime="video/mp4"
                )