class clear_m73:
    def __init__(self, config):
        self.printer = config.get_printer()
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('CLEAR_M73', self.cmd_CLEAR_M73, desc=self.cmd_CLEAR_M73_help)

    cmd_CLEAR_M73_help = "Release control of progress bar back to virtual sdcard"
    
    def cmd_CLEAR_M73(self, gcmd):
        display_status = self.printer.lookup_object('display_status')
        display_status.progress = None

def load_config(config):
    return clear_m73(config)
