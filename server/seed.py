from app import app, db, Bakery, BakedGood

with app.app_context():
    print("🌱 Seeding database...")

    db.drop_all()
    db.create_all()

    # Create one bakery
    bakery1 = Bakery(name="Test Bakery")
    db.session.add(bakery1)
    db.session.commit()

    # Add baked goods
    bg1 = BakedGood(name="Croissant", price=3, bakery_id=bakery1.id)
    bg2 = BakedGood(name="Baguette", price=5, bakery_id=bakery1.id)
    bg3 = BakedGood(name="Cake", price=10, bakery_id=bakery1.id)

    db.session.add_all([bg1, bg2, bg3])
    db.session.commit()

    print("✅ Done seeding!")
