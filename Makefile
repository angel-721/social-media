new:
	rm -rf ./database/database.db
	sqlite3 ./database/database.db < ./database/schema.sql

shell:
	sqlite3 ./database/database.db

add-user:
	./pyfiles/social_media.py --add-user 1

clean:
	rm -rf ./database/database.db
