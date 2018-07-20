#coding=utf-8
from test_runner.ranzhi_test_runner import RanzhiTestRunner


class Main(object):
    @staticmethod
    def start_ranzhi_test():
        RanzhiTestRunner().run()

if __name__=="__main__":
    Main.start_ranzhi_test()


#如果不用 @staticmethod
#  def start_ranzhi_test(self):
#       RanzhiTestRunner().run(None)