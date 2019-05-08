import json
import falcon

from app.utils.mDev import mDEV


class MotorResource(object):

    i2c_interface = mDEV()

    def on_put(self, req, resp):

        payload = json.loads(req.stream.read())
        speed = int(payload['speed'])
        direction = int(payload['direction'])

        self.i2c_interface.writeReg(self.i2c_interface.CMD_DIR1,direction)
        self.i2c_interface.writeReg(self.i2c_interface.CMD_DIR2,direction)

        self.i2c_interface.writeReg(self.i2c_interface.CMD_PWM1,speed)
        self.i2c_interface.writeReg(self.i2c_interface.CMD_PWM2,speed)


        resp.status = falcon.HTTP_202
