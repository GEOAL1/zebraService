# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25 by eric zhang

def login_required(f):
    def _wrapper(self, *args, **kwargs):
        logged = self.get_current_user()
        if logged == None:
            self.rediret("/login")
            self.finish()
        else:
            ret = f(self, *args, **kwargs)

    return _wrapper
