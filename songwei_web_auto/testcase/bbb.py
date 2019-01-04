class People():
    def __init__(self, a="girl", b="live"):
        self.friend = a
        self.live = b

    def hand(self):
        h = "这是我对象的手:%s and %s"%(self.friend, self.live)
        return(h)

    def foot(self):
        f = "这是我对象的脚:%s and %s"%(self.friend, self.live)
        return(f)


if __name__ == "__main__":

    a = People()
    b = People("boy")
    c = People(b="live")
    print(b.hand())
    print(c.hand())
