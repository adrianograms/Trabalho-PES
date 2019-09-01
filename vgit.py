from window import vgit_main
import gi
gi.require_version('Gtk', '3.0')

try:
    from gi.repository import Gtk
except ImportError:
    raise

if __name__ == "__main__":
    main = vgit_main()
    Gtk.main()
