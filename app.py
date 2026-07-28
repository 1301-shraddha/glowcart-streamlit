import streamlit as st
import pandas as pd

# ==============================
# PAGE SETTINGS
# ==============================

st.set_page_config(
    page_title="GlowCart AI",
    page_icon="💄",
    layout="wide"
)

# ==============================
# LOAD PRODUCTS
# ==============================

products = pd.read_csv("products.csv")
# ==============================
# CART
# ==============================

if "cart" not in st.session_state:
    st.session_state.cart = []

    # ==============================
# WISHLIST
# ==============================

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

    # ==============================
# RATINGS
# ==============================

if "ratings" not in st.session_state:
    st.session_state.ratings = {}

    # ==============================
# ORDER HISTORY
# ==============================

if "orders" not in st.session_state:
    st.session_state.orders = []

    # ==============================
# LOGIN SESSION
# ==============================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>

.main{
    background:#FFF5FA;
}

h1,h2,h3{
    color:#C2185B;
}

.stButton>button{
    background:#C2185B;
    color:white;
    border:none;
    border-radius:10px;
    width:100%;
    height:45px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#AD1457;
}

.product-card{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.15);
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# SIDEBAR
# ==============================

st.sidebar.image("images/logo.png", width=130)

st.sidebar.title("GlowCart")

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Shopping Cart")

st.sidebar.write(f"Items : {len(st.session_state.cart)}")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "👤 Login",

        "👤 Profile",

        "🛍 Products",

        "❤️ Wishlist",

        "🤖 AI Recommendation",

        "💬 AI Chatbot",

        "🛒 Cart",

        "💳 Payment",

        "✅ Order Confirmation",

        "📜 Order History",

        "📞 Contact",

    ]

)
# ==========================================================
# HOME PAGE
# ==========================================================

if page == "🏠 Home":

    st.markdown("""
    <div style="
    background:linear-gradient(90deg,#ff4d88,#ff99c8);
    padding:30px;
    border-radius:20px;
    text-align:center;
    color:white;
    ">
    <h1>💄 GlowCart AI</h1>
    <h3>Your Smart Beauty Shopping Destination</h3>
    <p>Discover Skincare • Makeup • Haircare • Perfumes</p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.logged_in:
        st.success(f"👋 Welcome back, {st.session_state.username}!")

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.image("images/cetaphil.jpg", use_container_width=True)
        st.markdown("### 🌿 Skincare")

    with c2:
        st.image("images/maybelline_foundation.jpg", use_container_width=True)
        st.markdown("### 💄 Makeup")

    with c3:
        st.image("images/loreal.jpg", use_container_width=True)
        st.markdown("### 💇 Haircare")

    with c4:
        st.image("images/bella_ceo.jpg", use_container_width=True)
        st.markdown("### 🌸 Perfume")

    st.write("---")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("🛍 Products", "30+")

    with m2:
        st.metric("🤖 AI", "Smart")

    with m3:
        st.metric("⭐ Rating", "4.8")

    with m4:
        st.metric("🚚 Delivery", "Free")

    st.write("---")

    st.subheader("🔥 Featured Products")

    featured = products.head(4)

    cols = st.columns(4)

    for i, (_, row) in enumerate(featured.iterrows()):

        with cols[i]:

            st.image(row["image"], use_container_width=True)

            st.write(f"**{row['name']}**")

            st.write(f"₹ {row['price']}")

            st.button("🛒 Buy Now", key=f"home_{i}")

            # ==========================================================
# LOGIN PAGE
# ==========================================================

elif page == "👤 Login":

    st.title("👤 Login / Signup")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    # ---------------- LOGIN ----------------

    with tab1:

        username = st.text_input("Username", key="login_user")

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
        )

        if st.button("Login"):

            if username != "" and password != "":

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success(f"Welcome {username} 🎉")

            else:

                st.error("Please enter username and password.")

    # ---------------- SIGNUP ----------------

    with tab2:

        new_user = st.text_input(
            "Create Username",
            key="signup_user"
        )

        new_pass = st.text_input(
            "Create Password",
            type="password",
            key="signup_pass"
        )

        if st.button("Create Account"):

            if new_user != "" and new_pass != "":

                st.success("🎉 Account Created Successfully!")

            else:

                st.error("Please fill all fields.")

    st.write("---")

    if st.session_state.logged_in:

        st.success(f"Logged in as **{st.session_state.username}**")

        if st.button("Logout"):

            st.session_state.logged_in = False
            st.session_state.username = ""

            st.success("Logged Out Successfully.")

            # ==========================================================
# PROFILE PAGE
# ==========================================================

elif page == "👤 Profile":

    st.title("👤 My Profile")

    if st.session_state.logged_in:

        st.success(f"Welcome, {st.session_state.username} 👋")

        st.write("---")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("❤️ Wishlist", len(st.session_state.wishlist))

        with col2:
            st.metric("🛒 Cart Items", len(st.session_state.cart))

        col3, col4 = st.columns(2)

        with col3:
            st.metric("📜 Orders", len(st.session_state.orders))

        with col4:
            st.metric("⭐ Reviews", len(st.session_state.ratings))

        st.write("---")

        if st.button("🚪 Logout"):

            st.session_state.logged_in = False
            st.session_state.username = ""

            st.success("Logged Out Successfully!")

    else:

        st.warning("⚠️ Please login first.")
            # ==========================================================
# PRODUCTS PAGE
# ==========================================================

elif page == "🛍 Products":

    st.title("🛍 Beauty Products")

    search = st.text_input("🔍 Search Product")

    category = st.selectbox(
        "Choose Category",
        ["All"] + sorted(products["category"].unique().tolist())
    )

    df = products.copy()

    if search:
        df = df[df["name"].str.contains(search, case=False, na=False)]

    if category != "All":
        df = df[df["category"] == category]

    if len(df) == 0:
        st.warning("No products found.")
    else:

        cols = st.columns(3)

        for i, (_, product) in enumerate(df.iterrows()):

            with cols[i % 3]:

                st.markdown(
                    """
                    <div class="product-card">
                    """,
                    unsafe_allow_html=True
                )

                st.image(
                    product["image"],
                    use_container_width=True
                )

                st.markdown(f"### {product['name']}")

                st.write(f"💰 **₹ {product['price']}**")

                st.write(f"📂 {product['category']}")

                st.write(f"✨ Skin Type: {product['skin_type']}")

                st.write("⭐⭐⭐⭐⭐")

                if st.button(
                    "🛒 Add to Cart",
                    key=f"cart_{i}"
                ):
                    st.session_state.cart.append(product.to_dict())
                    st.success(f"✅ {product['name']} added to cart!")

                if st.button(
    "❤️ Add to Wishlist",
    key=f"wish_{i}"
):

                  st.session_state.wishlist.append(product.to_dict())

                  st.success(f"{product['name']} added to Wishlist ❤️")
                if st.button(
                    "⚡ Buy Now",
                    key=f"buy_{i}"
                ):

                    st.session_state.buy_now = product.to_dict()

                    st.info("👉 Please open the 💳 Payment page from the sidebar.")
                st.write("### ⭐ Rate this Product")

                st.write("### ⭐ Rate this Product")

                rating = st.slider(
                    "Rating",
                    1,
                    5,
                    5,
                    key=f"rating_{i}"
                )

                review = st.text_input(
                    "Write Review",
                    key=f"review_{i}"
                )

                if st.button(
                    "Submit Review",
                    key=f"submit_{i}"
                ):

                    st.session_state.ratings[product["name"]] = {
                        "rating": rating,
                        "review": review
                    }

                    st.success("⭐ Review Submitted!")

                if product["name"] in st.session_state.ratings:

                    data = st.session_state.ratings[product["name"]]

                    st.success(f"⭐ {data['rating']}/5")
                    st.write(f"💬 {data['review']}")

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

# ==========================================================
# AI RECOMMENDATION
# ==========================================================


elif page == "🤖 AI Recommendation":

    st.title("🤖 AI Beauty Recommendation")

    st.write("Select your skin type and get the best products.")

    skin = st.selectbox(
        "Choose Your Skin Type",
        ["Oily", "Dry", "Normal", "All"]
    )

    if st.button("✨ Get Recommendation"):

        if skin == "All":
            recommend = products
        else:
            recommend = products[
                (products["skin_type"].str.lower() == skin.lower()) |
                (products["skin_type"].str.lower() == "all")
            ]

        cols = st.columns(3)

        for i, (_, product) in enumerate(recommend.iterrows()):

            with cols[i % 3]:

                st.image(product["image"], use_container_width=True)

                st.subheader(product["name"])

                st.write(f"₹ {product['price']}")

                st.write(product["category"])

                st.button(
                    "View Product",
                    key=f"rec{i}"
                )
# ==========================================================
# AI CHATBOT
# ==========================================================

elif page == "💬 AI Chatbot":

     st.title("💬 GlowBot")

     st.info("👋 Hello! Welcome to GlowCart.")

     st.write("### How can I help you today?")
 
     user = st.text_input("Ask anything about beauty products")

     if st.button("Send"):

        msg = user.lower()

        # Greeting
        if any(word in msg for word in ["hi", "hello", "hey"]):

            st.success("Hello 👋 Welcome to GlowCart! I can help you with skincare, makeup, haircare and perfumes.")

        # Oily Skin
        elif "oily" in msg:

            st.success("These products are recommended for Oily Skin:")

            rec = products[
                (products["skin_type"].str.lower()=="oily") |
                (products["skin_type"].str.lower()=="all")
            ]

            for _, p in rec.iterrows():

                st.image(p["image"], width=100)

                st.write(f"✅ {p['name']} - ₹{p['price']}")

        # Dry Skin
        elif "dry" in msg:

            st.success("These products are recommended for Dry Skin:")

            rec = products[
                (products["skin_type"].str.lower()=="dry") |
                (products["skin_type"].str.lower()=="all")
            ]

            for _, p in rec.iterrows():

                st.image(p["image"], width=100)

                st.write(f"✅ {p['name']} - ₹{p['price']}")

        # Normal Skin
        elif "normal" in msg:

            st.success("These products are recommended for Normal Skin:")

            rec = products[
                (products["skin_type"].str.lower()=="normal") |
                (products["skin_type"].str.lower()=="all")
            ]

            for _, p in rec.iterrows():

                st.image(p["image"], width=100)

                st.write(f"✅ {p['name']} - ₹{p['price']}")

        # Makeup
        elif any(word in msg for word in ["lipstick","foundation","makeup","kajal","mascara"]):

            st.success("Recommended Makeup Products:")

            rec = products[
                products["category"].str.lower()=="makeup"
            ]

            for _, p in rec.iterrows():

                st.image(p["image"], width=100)

                st.write(f"💄 {p['name']} - ₹{p['price']}")

        # Haircare
        elif any(word in msg for word in ["hair","hairfall","shampoo","conditioner"]):

            st.success("Recommended Haircare Products:")

            rec = products[
                products["category"].str.lower()=="haircare"
            ]

            for _, p in rec.iterrows():

                st.image(p["image"], width=100)

                st.write(f"💇 {p['name']} - ₹{p['price']}")

        # Perfume
        elif any(word in msg for word in ["perfume","deo","fragrance"]):

            st.success("Recommended Perfumes:")

            rec = products[
                products["category"].str.lower()=="perfume"
            ]

            for _, p in rec.iterrows():

                st.image(p["image"], width=100)

                st.write(f"🌸 {p['name']} - ₹{p['price']}")

        else:

            st.warning("""
Sorry 😔

I can help you with:

• Oily Skin

• Dry Skin

• Normal Skin

• Makeup

• Haircare

• Perfume

• Lipstick

• Foundation

Please ask beauty related questions.
""")
# ==========================================================
# CART PAGE
# ==========================================================

elif page == "🛒 Cart":

    st.title("🛒 Shopping Cart")

    if len(st.session_state.cart) == 0:

        st.warning("Your cart is empty.")

    else:

        total = 0

        for i, product in enumerate(st.session_state.cart):

            col1, col2 = st.columns([1,3])

            with col1:

                st.image(product["image"], width=120)

            with col2:

                st.subheader(product["name"])

                st.write(f"₹ {product['price']}")

                total += int(product["price"])

                if st.button(
                    "❌ Remove",
                    key=f"remove{i}"
                ):

                    st.session_state.cart.pop(i)

                    st.rerun()

            st.write("---")

        st.success(f"💰 Total Amount : ₹ {total}")

        if st.button("✅ Checkout"):

            st.balloons()

            st.success("🎉 Order Placed Successfully!")

            # ==========================================================
# PAYMENT PAGE
# ==========================================================

elif page == "💳 Payment":

    st.title("💳 Payment")

    if "buy_now" not in st.session_state:

        st.warning("⚠️ Please select a product using Buy Now.")

    else:

        product = st.session_state.buy_now

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(product["image"], width=180)

        with col2:
            st.subheader(product["name"])
            st.write(f"💰 Price: ₹{product['price']}")
            st.write(f"📂 Category: {product['category']}")

        st.write("---")

        payment = st.radio(
            "Select Payment Method",
            [
                "💵 Cash on Delivery",
                "📱 UPI",
                "💳 Credit / Debit Card"
            ]
        )

        if payment == "📱 UPI":
            st.text_input("Enter UPI ID")

        elif payment == "💳 Credit / Debit Card":
            st.text_input("Card Number")
            st.text_input("Card Holder Name")
            st.text_input("Expiry (MM/YY)")
            st.text_input("CVV", type="password")

        if st.button("✅ Place Order"):

           st.session_state.order = product
           st.session_state.orders.append(product)

    st.balloons()

    st.success("🎉 Order Placed Successfully!")

    st.info("👉 Open '✅ Order Confirmation' from the sidebar.")

    # ==========================================================
# ORDER CONFIRMATION
# ==========================================================

elif page == "✅ Order Confirmation":

    st.title("🎉 Order Confirmed")

    if "order" not in st.session_state:

        st.warning("No order found.")

    else:

        product = st.session_state.order

        st.success("Your order has been placed successfully!")

        st.image(product["image"], width=180)

        st.subheader(product["name"])

        st.write(f"💰 Price : ₹ {product['price']}")

        st.write("📦 Estimated Delivery : 3-5 Days")

        st.write("🆔 Order ID : GC10245")

        st.write("---")

        st.markdown("## ❤️ Thank You For Shopping With GlowCart!")

        if st.button("🏠 Continue Shopping"):

            del st.session_state.order

            st.success("You can continue shopping from the Products page.")

            # ==========================================================
# WISHLIST
# ==========================================================

elif page == "❤️ Wishlist":

    st.title("❤️ My Wishlist")

    if len(st.session_state.wishlist) == 0:

        st.warning("Wishlist is Empty.")

    else:

        cols = st.columns(3)

        for i, product in enumerate(st.session_state.wishlist):

            with cols[i % 3]:

                st.image(product["image"])

                st.subheader(product["name"])

                st.write(f"₹ {product['price']}")

                if st.button(
                    "❌ Remove",
                    key=f"wishremove{i}"
                ):

                    st.session_state.wishlist.pop(i)

                    st.rerun()

                    # ==========================================================
# ORDER HISTORY
# ==========================================================

elif page == "📜 Order History":

    st.title("📜 My Orders")

    if len(st.session_state.orders) == 0:

        st.warning("No orders placed yet.")

    else:

        for i, product in enumerate(st.session_state.orders):

            col1, col2 = st.columns([1,3])

            with col1:
                st.image(product["image"], width=120)

            with col2:
                st.subheader(product["name"])
                st.write(f"💰 ₹ {product['price']}")
                st.write(f"📂 {product['category']}")
                st.success("✅ Delivered")

            st.write("---")

 # ==========================================================
# CONTACT PAGE
# ==========================================================

elif page == "📞 Contact":

    st.title("📞 Contact GlowCart")

    st.write("We would love to hear from you ❤️")

    st.write("📍 Pune, Maharashtra")

    st.write("📧 support@glowcart.com")

    st.write("📞 +91 9876543210")

    st.write("---")

    st.subheader("Send us a Message")

    name = st.text_input("Your Name")

    email = st.text_input("Your Email")

    message = st.text_area("Message")

    if st.button("Send Message"):

        st.success("✅ Thank you! Your message has been received.")
        # ==========================================================
# FOOTER
# ==========================================================

st.write("---")

st.markdown(
    """
    <div style='text-align:center;color:gray;padding:20px'>
    💄 <b>GlowCart AI Beauty Store</b><br><br>

    Built with ❤️ using Streamlit<br>

    © 2026 GlowCart. All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True
)