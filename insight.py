import streamlit as st

def insight_page():
    st.title("Insight Page")

    for i in range(1, 11):
        st.markdown(f"### Insight {i}")

        st.text(f"This is your {i} insight.")
        
        # Create two columns for buttons
        col1, col2 = st.beta_columns(2)

        # Add unique keys to the buttons
        like_button = col1.button("Like", key=f"like_button_{i}")
        dislike_button = col2.button("Dislike", key=f"dislike_button_{i}")
        share_button = col1.button("Share", key=f"share_button_{i}")
        bookmark_button = col2.button("Bookmark", key=f"bookmark_button_{i}")

        # You can handle the button actions here as needed
        if like_button:
            # Handle the Like action for insight i
            pass

        if dislike_button:
            # Handle the Dislike action for insight i
            pass

        if share_button:
            # Handle the Share action for insight i
            pass

        if bookmark_button:
            # Handle the Bookmark action for insight i
            pass
