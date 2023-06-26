"""
 * @author        yasir <yasiramunandar@gmail.com>
 * @date          2022-09-06 10:12:09
 * @projectName   MissKatyPyro
 * Copyright @YasirPedia All rights reserved
"""
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from Himawari.__init__ import DB_URL

mongo = MongoClient(DATABASE_URI)
dbname = mongo.MissKatyDB
