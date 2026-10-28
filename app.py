from flask import flask, render_template

app-flask(__name__)

@app.toute(´/´)
def inicio():
  return render_template(´index.html´)

if __name__--__main__´:
  app.run(debug-true)
