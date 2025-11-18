from typing import List

from fastapi.exceptions import FastAPIError

from src.packages.user.model import User
from fastapi import Request
from sqlmodel import select, func

class UserDal:

    def __init__(self, session):
        self.session = session

    # can do single insert and bulk insert
    def add(self, new_users: List[User]):
        try:
            result = []

            # new_users = [u1 , u2, u3]
            for user in new_users:
                self.session.add(user)

            self.session.commit()

            for student in new_users:
                self.session.refresh(user)
                result.append(user)

            return result

        except Exception as error:
            self.session.rollback()
            print("Unexpected Error : ", str(error))



    def get_all(self, request_model: Request, offset:int, limit:int):
        try:
            statement = select(User)

            if offset is not None and limit is not None:
                page = (offset -1)*limit
                statement = statement.order_by(User.id.desc()).offset(page).limit(limit)
            else:
                pass

            records = self.session.exec(statement=statement).all()
            # data = [Student, Student, Student, Student, Student, Student]

            count_statement = select(func.count()).select_from(User)
            total_count = self.session.exec(count_statement).one()

            return records, total_count

        except Exception as error:
            print("Unexpected Error : ", str(error))

    def get_by_id(self, r_id: int):
        try:
            record = self.session.get(User, r_id)
            return record
        except Exception as error:
            print("Unexpected Error : ", str(error))


    def update_by_id(self, r_id: int, body):
        try:
            record = self.session.get(User, r_id)
            if record is None:
                return False, None
            else:
                record.sqlmodel_update(body.model_dump(exclude_unset=True))
                self.session.add(record)
                self.session.commit()
                self.session.refresh(record)
                return True, record
        except Exception as error:
            self.session.rollback()
            print("Unexpected Error : ", str(error))

    def delete_by_id(self, r_id: int):
        try:
            record = self.session.get(User, r_id)
            if record is None:
                return False, None
            else:
                self.session.delete(record)
                self.session.commit()
                return True, record
        except Exception as error:
            self.session.rollback()
            print("Unexpected Error : ", str(error))