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

<h3>
    <a id="user-content-home-page" class="anchor" aria-hidden="true" href="#home-page"></a>
Home Page
</h3>

<p>The home page give the user a list of 24 recipes which are stored inside the Mongo database.  By clicking any recipe it will give you a brief description of what the recipe is about.  The recipe will popout and be shaded so the user will be able to read the details clearly but still remain on the page and by simply clicking the unlighted area the popout will close.  Very simple and straightforward use of the materialize framework.</p>
<p>There are also two buttons available, these are delete and edit, both of which both work - <strong>Be very careful - As these will affect the information stored at the database.</strong>See further information at features left to implement section.</p>

<h3>
    <a id="user-content-new-recipe" class="anchor" aria-hidden="true" href="#new-recipe"></a>
New Recipe
</h3>

<p>By clicking the New Recipe link on the navbar, the Add Recipe page opens to a new form which has 5 fields which the user can fill out with information.  The first field gives the user a choice of categories which are already built into the site.  If the category the user wants to use is not listed, the user can select Manage Categories on the navbar and create a new one (see manage categories later in the document)</p>
<p>The second form field gives the user the opportunity to name the recipe,  the user must be careful when naming the recipe as not to duplicate it with another as this would cause confusion to other users but one would imagine a user would ensure that the recipe name would be unique.</p>
<p>The next form field gives the user the opportunity to give their recipe a description, this is where the user can use this form field as a strap line to promote the recipe and hopefully catch the eye of the other users.</p>
<p>The next form field gives the user to input all ingredients required to create the recipe, this would include quantities, special named ingredients etc.</p>
<p>The final form field gives the user to list in order how to put the recipe together, this would include cooking times, prepatation of ingredients, any cooking tips they would like to share and how to serve the final product.</p>
<p>There at the bottom of the page is a button where the user can click and the recipe will be added to the database</p>

<h3>
    <a id="user-content-manage-categories" class="anchor" aria-hidden="true" href="#manage-categories"></a>
</h3>

<p>


