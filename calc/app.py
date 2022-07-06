from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/')
def home():
    html =  """
    <html>
        <body>
            <h1> Home Page </h1>
            <p> My home page</p>
            <a href='/add'> Go to add page</a>
            <a href='/sub'> Go to subtract page</a>
            <a href='/mult'> Go to multiply page</a>
            <a href='/div'> Go to divide page</a>
        </body>
    </html>
    """
    return html


# @app.route("/add")
# def add():
#     return """
#     <h1> This page will add A and B together <h1>
#     <form >
#         <input type='number' placeholder='A' name='a'/>
#         <input type='number' placeholder='B' name='b'/>
#         <button> Add </button>
#     </form>
#     """
    

@app.route("/add")
def sum():
    """ handling adding, taking input, putting it into variables and adding them together """
    a = int(request.args["a"])
    print(a)
    b = int(request.args["b"])
    print(b)

   
    return f"""{int(operations.add(a,b))} """



# @app.route("/sub")
# def subtract():
#     return """
#     <h1> This page will subtract B from A <h1>
#         <form method="POST">
#             <input type='text' placeholder='A' name='a'/>
#             <input type='text' placeholder='B' name='b'/>
#             <button> Subtract </button>
#         </form>
#     """
    
   
@app.route("/sub")
def difference():
    """ handling subtraction, taking input, putting it into variables and adding them together """
    a = int(request.args["a"])
    
    b = int(request.args["b"])
    

    return f""" {int(operations.sub(a,b))} """


# @app.route("/mult")
# def multiply():
#     return """
#     <h1>This page will multiply the numbers<h1>
#     <form method="POST">
#         <input type='text' placeholder='A' name='a'/>
#         <input type='text' placeholder='B' name='b'/>
#         <button> Add </button>
#     </form>
#     """

    

@app.route("/mult")
def product():
    """ handling adding, taking input, putting it into variables and adding them together """
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f""" {int(operations.mult(a,b))} """


# @app.route("/div")
# def divide():
#     return """
#     <h1> This page will divide numbers<h1>
#     <form method="POST">
#         <input type='text' placeholder='A' name='a'/>
#         <input type='text' placeholder='B' name='b'/>
#         <button> Divide </button>
#     </form>
#     """
    


@app.route("/div")
def dividend():
    """ handling adding, taking input, putting it into variables and adding them together """
    a = int(request.args["a"])
    b = int(request.args["b"])



    return f"""{int(operations.div(a,b))} """