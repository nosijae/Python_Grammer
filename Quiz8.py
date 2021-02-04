class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("총 {0}대의 매물이 있습니다.".format(len(self)))
        for house in self:
            print(house.location, house.house_type, house.deal_type, \
                  house.price, house.completion_year)


house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

Houses = [house1, house2, house3]

House.show_detail(Houses)
