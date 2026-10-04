class android:
    def features(self):
        print("Customizable home screen")
class iphone:
    def features(self):
        print("Face ID on supported models")
class  Windows_phone:
    def features(self):
        print("Live tiles on the home screen")
a =android()
i = iphone()
w = Windows_phone()
a.features()
i.features()
w.features()