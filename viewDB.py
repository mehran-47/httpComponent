#!/usr/bin/env python3
import shelve as sh
if __name__ == '__main__':
	try:
		db = sh.open('/opt/SA_stats/compDB.db')
		for key in db: print(key + " : " + str(db[key]))
	finally:
		db.close()