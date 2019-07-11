import sublime
import sublime_plugin

class I18nCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      def on_done(key):
        string = self.view.substr(region);
        self.view.run_command("insert", {"characters": 't(".' + key +'")'})
        self.view.run_command("move_to", {"to": "eol"})
        self.view.run_command("insert", {"characters": "\n" + key + ": " + string})
      window = self.view.window()
      window.show_input_panel("Key name:", "", on_done, None, None)
