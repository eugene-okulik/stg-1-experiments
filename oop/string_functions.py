class StringFunctions:

    def remove_o(self, text: str):
        return text.replace('o', '')

    def remove_x(self, text: str):
        return text.replace('x', '')


without_o = StringFunctions().remove_o('sldkfowijsdkfsowekjhsdf')
print(without_o)


class bouquet:

    def __init__(self, flowers_list):
        self.flow_list = flowers_list

fl1 = ''
lf2 = ''
bouq1 = bouquet([fl1, lf2])