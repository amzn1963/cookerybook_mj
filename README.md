<h1>
<a id="user-content-MJ's-GoodFood" class="anchor" aria-hidden="true" href="#MJ's-GoodFood"></a>
MJ's GoodFood</h1>

<p>This is the 3rd Milestone Project of which data has been created in the form of recipes and varying categories in order to produce a simple cookbook.  There are 8 different categories and a total of 22 different recipes, these all have a recipe name, recipe description, recipe ingredients and cooking instructions.  The categories range from quick and easy to healthy and cuisines from around the world.</p>

<h2>
<a id="user-content-table-of-contents" class="anchor" area-hidden="true" href="#table-of-contents"></a>
Table of Contents</h2>
<ol start="2">
    <li>
    <a href="#ux">UX</a>
    </li>
    <li>
    <a href="#features">FEATURES</a>
        <ol>
    <li>
    <a href="#home-page">Home Page</a>
    </li>
    <li>
    <a href="#new-recipe">New Recipe</a>
    </li>
    <li>
    <a href="#manage-categories">Manage Categories</a>
    </li>
    <li>
    <a href="#contact-page">Contact Page</a>
    </li>
    <li>
    <a href="navbar">Navbar</a>
    </li>
        </ol>
    <li>
    <a href="#features-left-to-implement">FEATURES LEFT TO IMPLEMENT</a>
    </li>
    <li>
    <a href="#technologies-used">TECHNOLOGIES USED</a>
    </li>
    <li>
    <a href="#testing">TESTING</a>
    </li>
    <li>
    <a href="#deployment">DEPLOYMENT</a>
    </li>
    <li>
    <a href="#credits">CREDITS</a>
    </li>
</ol>
<h2>
    <a id="user-content-ux" class="anchor" aria-hidden="true" href="#ux"></a>
UX
</h2>

<p>The project required building a data driven web application using the technologies learned throughout the Data Centric Development modules.  This being the premise, a database schema were designed based on recipes and other related properties such as categories i.e - Quick and Easy, worldwide cuisines, healthy and such like.  It also included ingredients and method of cooking, special tips to assist the user.</p>
<p>The backend code allows the user to add recipes and categories through the frontend forms and each form has a variety of popout input blocks.  It also has the facility to edit both the categories and recipes if required, the data is saved at the Mongo Database.  Using Materialize framework at the frontend incorporating subtle styling gives the user a clean look to the page.</P>

<h2>
    <a id="user-content-features" class="anchor" aria-hidden="true" href="#features"></a>
FEATURES
</h2>

<p>Firstly, the user can input a new recipe by clicking the link on the navbar (see more information regarding new recipe in a later section).</p>
<p>Secondly, the user can manage categories by also clicking the link in the navbar (see more information regarding new recipe in a later section).</p>
<p>Thirdly, there are edit and delete buttons the user can use to assist them when using the site.</p>
<p>Finally, there is a slideout facility which gives the user information to contact the website designer for any queries/questions.</p>

<ol>
    <li>
<h3>
    <a id="user-content-home-page" class="anchor" aria-hidden="true" href="#home-page"></a>
Home Page
</h3>

<p>The home page give the user a list of 24 recipes which are stored inside the Mongo database.  By clicking any recipe it will give you a brief description of what the recipe is about.  The recipe will popout and be shaded so the user will be able to read the details clearly but still remain on the page and by simply clicking the unlighted area the popout will close.  Very simple and straightforward use of the materialize framework.</p>
<p>There are also two buttons available, these are delete and edit, both of which both work - <strong>Be very careful - As these will affect the information stored at the database.</strong> See further information at features left to implement section.</p>
    </li>
    <li>
<h3>
    <a id="user-content-new-recipe" class="anchor" aria-hidden="true" href="#new-recipe"></a>
New Recipe
</h3>

<p>By clicking the New Recipe link on the navbar, the Add Recipe page opens to a new form which has 5 fields which the user can fill out with information.  The first field gives the user a choice of categories which are already built into the site.  If the category the user wants to use is not listed, the user can select Manage Categories on the navbar and create a new one (see manage categories later in the document)</p>
<p>The second form field gives the user the opportunity to name the recipe,  the user must be careful when naming the recipe as not to duplicate it with another as this would cause confusion to other users but one would imagine a user would ensure that the recipe name would be unique.</p>
<p>The next form field gives the user the opportunity to give their recipe a description, this is where the user can use this form field as a strap line to promote the recipe and hopefully catch the eye of the other users.</p>
<p>The next form field gives the user to input all ingredients required to create the recipe, this would include quantities, special named ingredients etc.</p>
<p>The final form field gives the user to list in order how to put the recipe together, this would include cooking times, preparation of ingredients, any cooking tips they would like to share and how to serve the final product.</p>
<p>There at the bottom of the page is a button where the user can click and the recipe will be added to the database</p>
    </li>
    <li>
<h3>
    <a id="user-content-manage-categories" class="anchor" aria-hidden="true" href="#manage-categories"></a>
</h3>

<p>There are a total 8 different categories the user can choose from ranging from 'quick and easy' to 'cuisines' which showcase dishes from around the world.</p>
<p>There are also three buttons to assist the user when using this part of the website.</p>
<p>The first button is the delete button.  This will delete the category from the database. <strong>This button is active and should not be used until safeguards have been put in place</strong>. (This will explained later in the Features left to implement section).</p>
<p>The second button is the edit button.  This will edit the category within the database - as previously mentioned, the button is active and should again be used with caution.</p>
<p>The third button is the add category button which the user can create a brand new category for which their recipe would align with.  Again this button is active and would advise the reader to check 'Features left to implement' section prior to use.</p>
    </li>
    <li>
<h3>
    <a id="user-content-contact-page" class="anchor" aria-hidden="true" href="#contact-page"></a>
</h3>

<p>At the top left below the navbar on every page there is burger bar which when clicked information is produced via a slide out option.  There are 4 item listed vertically: home, new recipe, manage categories and login.  The first three items act as a navbar where the last item is not active but placed there for future development.</p>
<p>I have attached an image of myself and a dining table laid out - to keep in the theme of cookery.  This is little addon touch to give the user a better feel to the site.</p>
    </li>
    <li>
<h3>
    <a id="user-content-navbar" class="anchor" aria-hidden="true" href="#navbar"></a>
</h3>

<p>The navbar which is mounted at the top of the page has a few features which help the user in their actions whenusing the site.  Firstly, there is the title of the website - but it also acts as a link to the home page. This comes in handy for the user just to click the name instead of moving across to the other selections that are available.</P>
<p>When moving across to the right hand side of the navbar there are three options the user can click.  Firstly the home page link which is essential.  Secondly there is the 'New Recipe' link which takes the user to the new recipe page and finally the 'Manage Categores' link which again will take the user to the edit category page.</p>
<p>This navbar stays at the home of every page the user will visit so the user cannot get lost in the site.</p>
    </li>
</ol>
<h2>
    <a id="user-content-features-left-to-implement" class="anchor" aria-hidden="true" href="#features-left-to-implement"></a>
</h2>

<p>As this site is designed for users to read about existing recipes within a variety of categories, there are options for users to contribute their own recipes which will be shared with other users.</p>
<p>With recipes it is always good to supply a picture of the finished product - displayed in way that users will find it pleasing on the eye.  Unfortunately, the course work leading up to this project did not cover uploading of pictures with MongoDB but with further training, I am confident these can be added</p>
<p>Also, for a user who is just viewing the site, all add, edit and delete buttons become inactive unless the user has logged in.  This leads to a proper user registration page with passwords which the user can change - either Google Mail or another service.</p>
<p>Leading on from registration this will also give the user an opportunity to score recipes - either via star rating or by voting.
With registration being enabled the user can add a recipe, edit their own recipes or delete their recipes - this gives more control and prevents other user deleting other users recipes.</p>
<p>Also with users - incorporating some sort of blog page - users can interact with each other - share tips, using different ingredients to suit users around the world etc.</p>
    
<h2>
    <a id="user-content-technologies-used" class="anchor" aria-hidden="true" href="#technologies-used"></a>
</h2>

<p>The framework used was materialize (see link https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css) which also gave me the CSS stylesheets that was required. These gave me the structure that I required. I was impressed by one of the tutorials demonstrating different fonts and therefore I included fontawesome (see link https://fontawesome.com/). For the slide out - there is code already available at the Materialize page which basically was a copy and paste exercise with minimal additions. There is also scripts from cdnjs giving the necessary jquery - (see link https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.0/jquery.min.js and https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js) All the technologies used was encouraged by various tutors in the modules and using their knowledge and experience it was very useful. Not only the usefulness but also an understanding a new coder needs to learn and implement with confidence.</p>
    

<h2>
   <a id="user-content-testing" class="anchor" aria-hidden="true" href="#testing"></a>
</h2>

<p>Using Chrome as my default browser I used its development tools to check the responsiveness of the website through various screen sizes. I have run the CSS through a validation site (see link https://jigsaw.w3.org/css-validator/).</p>
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
    
<h2>
    <a id="user-content-deployment" class="anchor" aria-hidden="true" href="#deployment"></a>
</h2>

<p>This site is hosted using GitHub pages, deployed directly from the master branch. The deployed site will update automatically upon new commits to the master branch. In order for the site to deploy correctly on GitHub pages, the landing page must be named index.html.
To run locally, you can clone this repository directly into the editor of your choice by pasting git clone https://amzn1963.github.io/cookerybook_mj/ into your terminal. To cut ties with this GitHub repository, type git remote rm origin into the terminal.</p>
<p>Using Heroku - auto build and deploy has been activated - this gives an active web address https://mj-cookerybook.herokuapp.com/get_recipes

<h2>
    <a id="user-content-credits" class="anchor" aria-hidden="true" href="#credits"></a>
</h2>

<p>All recipes and the related categories were found on the BBC Food Website https://www.bbcgoodfood.com/</p>
<p>All styling were utiilized using the Materialize framework.</p>


 


