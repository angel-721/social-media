shell:
	sqlite3 ./database/database.db;

add-user:
	cd ./pyfiles; python social_media.py --add-user 1;

delete-user:
	cd ./pyfiles; python social_media.py --delete-user 1;

follow-user:
	cd ./pyfiles; python social_media.py --follow-user 1;

post:
	cd ./pyfiles; python social_media.py --post 1;

feed:
	cd ./pyfiles; python social_media.py --feed 1;
recommendations:
	cd ./pyfiles; python social_media.py --bacon-feed 1;

search-feed:
	cd ./pyfiles; python social_media.py --search-feed 1;

clean:
	rm -rf ./database/database.db;
	sqlite3 ./database/database.db < ./database/schema.sql
