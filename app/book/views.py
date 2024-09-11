from flask import render_template, request, redirect, url_for, Blueprint

from werkzeug.utils import secure_filename
import os

from app.models import db, Books

from app.book import books_blueprint
from app.book.forms import BooksForm


@books_blueprint.route("/", endpoint="index")
def books_list():
    books = Books.query.all()
    return render_template("books/index.html", books=books)


@books_blueprint.route("/create", endpoint="create", methods=["GET", "POST"])
def books_create():
    form = BooksForm()
    if form.validate_on_submit():
        image_filename = secure_filename(form.image.data.filename) if form.image.data else "default_image.png"
        print(image_filename)
        if form.image.data:
            form.image.data.save(os.path.join('app/static/images', image_filename))

        book = Books(
            title=form.title.data,
            description=form.description.data,
            pages=form.pages.data,
            image=image_filename
        )
        db.session.add(book)
        db.session.commit()

        return redirect(url_for('books.index')) 

    return render_template('books/create.html', form=form)


@books_blueprint.route('/edit/<int:id>', endpoint="edit", methods=['GET', 'POST'])
def books_edit(id):
    book = Books.query.get_or_404(id)
    form = BooksForm()

    if form.validate_on_submit():
        book.title = form.title.data
        book.description = form.description.data
        book.pages = form.pages.data

        if form.image.data:
            image_filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join('app/static/images', image_filename))
            book.image = image_filename

        db.session.commit() 
        return redirect(url_for('books.index', id=book.id))

    elif request.method == 'GET':
        form.title.data = book.title
        form.description.data = book.description
        form.pages.data = book.pages
        # form.image.data.filename = book.image

    return render_template('books/create.html', form=form, book=book)


@books_blueprint.route("/show/<int:id>", endpoint="show")
def book_show(id):
    book = db.get_or_404(Books, id)
    return render_template("books/show.html", book=book)


@books_blueprint.route("<int:id>/delete", endpoint="delete", methods=["POST"])
def book_delete(id):
    book = db.get_or_404(Books, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books.index"))