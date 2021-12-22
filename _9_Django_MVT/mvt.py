'''1.Django MVT:

The MVT (Model View Template) is a software design pattern.
It is a collection of three important components Model View and Template.
The Model helps to handle database. It is a data access layer which handles the data.

The Template is a presentation layer which handles User Interface part completely.
The View is used to execute the business logic and interact with a model to carry
data and renders a template.

Although Django follows MVC pattern but maintains it?s own conventions. So,
control is handled by the framework itself.

There is no separate controller and complete application is based on Model
View and Template. That?s why it is called MVT application.

a user requests for a resource to the Django, Django works as a controller
and check to the available resource in URL.

If URL maps, a view is called that interact with model and template,
it renders a template.Django responds back to the user and sends a template as a response.

'''