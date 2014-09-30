from artiq import *


class SimpleSimulation(AutoContext):
    parameters = "a b c d"

    @kernel
    def run(self):
        with parallel:
            with sequential:
                self.a.pulse(100*MHz, 20*us)
                self.b.pulse(200*MHz, 20*us)
            with sequential:
                self.c.pulse(300*MHz, 10*us)
                self.d.pulse(400*MHz, 20*us)


if __name__ == "__main__":
    from artiq.sim import devices as sd
    from artiq.sim import time

    exp = SimpleSimulation(
        core=sd.Core(),
        a=sd.WaveOutput(name="a"),
        b=sd.WaveOutput(name="b"),
        c=sd.WaveOutput(name="c"),
        d=sd.WaveOutput(name="d"),
    )
    exp.run()
    print(time.manager.format_timeline())
