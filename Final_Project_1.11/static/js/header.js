document.addEventListener("DOMContentLoaded", function() {
    var headerHTML = `
    <head>
        <!--logo-->
        <div class="logo">
            <a href="index.html">Tales and Tomes Emporium</a>
        </div>
        <input type="checkbox" id="click">
        <label for="click" class="mainicon">
            <div class="menu">
                <i class="bi bi-list"></i>
            </div> 
    </head>
    <header>
    
        <nav>
            <ul class="main-menu">
                <a href="http://localhost:5000/home" class="active">Home</a>
                <a href="http://localhost:5000/aboutus">About Us</a>
                <!-- Categories Sub-Menu -->
                <li class="categories-dropdown">
                    <a href="javascript:void(0)">Categories</a>
                    <ul class="categories-dropdown-content">
                        <li><a href="http://localhost:5000/biography">Biography</a></li>
                        <!-- Other Categories -->
                        <li><a href="http://localhost:5000/mystery">Mystery</a></li>
                        <li><a href="http://localhost:5000/non_fiction">Non-fiction</a></li>
                        <li><a href="http://localhost:5000/fiction">Fiction</a></li>
                        <li><a href="http://localhost:5000/fantasy">Fantasy</a></li>
                        <li><a href="http://localhost:5000/thriller">Thriller</a></li>
                        <li><a href="http://localhost:5000/romance">Romance</a></li>
                        <li><a href="http://localhost:5000/young_adult">Young Adult</a></li>
                        <li><a href="http://localhost:5000/drama">Drama</a></li>
                        <li><a href="http://localhost:5000/natural_disaster">Natural Disaster</a></li>
                        <li><a href="http://localhost:5000/crime">Crime</a></li>
                        <li><a href="http://localhost:5000/adventure">Adventure</a></li>
                        <li><a href="http://localhost:5000/philosophy">Philosophy</a></li>
                        <li><a href="http://localhost:5000/psychological">Psychological</a></li>
                        <li><a href="http://localhost:5000/horror">Horror</a></li>
                        <li><a href="http://localhost:5000/travel">Travel</a></li>
                    </ul>
                </li>
                <a href="http://localhost:5000/contact">Contact Us</a>
            </ul>
        </nav>
        <!--login and signup button-->
        <div class="button">
            <li class="account-dropdown">
                <a href="javascript:void(0)">
                    <button>Account</button>
                </a>
                <div class="account-dropdown-content">
                    <a href="http://localhost:5000/create_account">Create Account</a>
                    <a href="http://localhost:5000/login">Log In</a>
                    <a href="http://localhost:5000/orders">Orders</a>
                    <a href="cart.html">Cart</a>
                </div>
            </li>
        </div>
    </header>
    `;
    document.body.insertAdjacentHTML('afterbegin', headerHTML);
});
