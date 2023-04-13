from flask import Flask, request, url_for

app = Flask(__name__)
#http://127.0.0.1:8080/greeting/Lera
#http://127.0.0.1:8080/sample_file_upload2


@app.route('/sample_file_upload2')
def sample_file_upload2():
    return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                 <link rel="stylesheet"
                                 href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                 integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                 crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пейзажи Марса</title>
                              </head>
                              <body>
                                <div id="carouselExampleCaptions" class="carousel slide">
                                <h1>Пейзажи Марса</h1>
                                <div id="carouselExampleIndicators" class="carousel slide">
                                  <div class="carousel-indicators">
                                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                                  </div>
                                  <div class="carousel-inner">
                                    <div class="carousel-item active">
                                      <img src="/static/one.jpg" class="d-block w-100" alt="...">
                                    </div>
                                  <div class="carousel-inner">
                                    <div class="carousel-item active">
                                      <img src="/static/two.png" class="d-block w-100" alt="...">
                                    </div>
                                  <div class="carousel-inner">
                                    <div class="carousel-item active">
                                      <img src="/static/three.png" class="d-block w-100" alt="...">
                                    </div>
                                  </div>
                                  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                    <span class="visually-hidden">Previous</span>
                                  </button>
                                  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                    <span class="visually-hidden">Next</span>
                                  </button>
                                </div>
                                </form>
                              </body>
                            </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')



