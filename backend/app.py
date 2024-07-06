from backend import create_app

app = create_app()

if __name__ == '__main__':
    import os
    with app.app_context():
        from backend.models import db
        db.create_all()
    app.run(debug=True)
