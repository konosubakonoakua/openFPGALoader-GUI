# %%
import os
import yaml
from rich.console import Console
from rich.pretty import Pretty

console = Console()

# %%
DEBUG = False

# openFPGALoader -c digilent_hs2 --fpga-part xc7k325tffg900 -f $MCS_FILE --verbose-level 2


_all_data = {}

folder_path = "../openFPGALoader/doc/"


def read_yaml(file_path):
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        console.print(f"File does not exist: {file_path}", style="bold red")
        return None

    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
            return data
    except yaml.YAMLError as e:
        console.print(f"Error parsing YAML file {file_path}: {e}", style="bold red")
        return None


def parse_cable(data: dict):
    return list(data.keys())


def parse_fpga(data: dict):
    pass


def parse_board(data: list):
    return [i["ID"] for i in data]


def print_dict_with_rich(data, title):
    if data is None:
        console.print(f"{title} is empty or could not be parsed.", style="bold yellow")
    else:
        console.print(f"{title}:", style="bold green")
        console.print(Pretty(data))


def get_all_data():
    all_data = {}

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        console.print(f"The folder '{folder_path}' does not exist.", style="bold red")
        return

    files_to_read = ["cable", "boards"]

    for file_name in files_to_read:
        file_path = os.path.join(folder_path, f"{file_name}.yml")
        data = read_yaml(file_path)
        all_data[file_name] = data
        if DEBUG:
            print_dict_with_rich(
                data, f"Contents of {file_name} (parsed as Python dictionary)"
            )

    return all_data


# %%
# _all_data = get_all_data()
# BOARDS = parse_board(_all_data["boards"])
# CABLES = parse_cable(_all_data["cable"])
BOARDS = [
    "LD-KONFEKT",
    "LD-SCHOKO",
    "SPEC150",
    "SPEC45",
    "VMM3",
    "ac701",
    "acornCle215",
    "alchitry_au",
    "alchitry_au_plus",
    "alinx_ax516",
    "alinx_ax7101",
    "alinx_ax7102",
    "analogMax",
    "antmicro_ddr4_tester",
    "antmicro_ddr5_tester",
    "antmicro_lpddr4_tester",
    "arty",
    "arty",
    "arty_a7_100t",
    "arty_a7_35t",
    "arty_s7_25",
    "arty_s7_50",
    "arty_z7_10",
    "arty_z7_20",
    "axu2cga",
    "basys3",
    "c10lp-refkit",
    "c5g",
    "certusnx_versa_evn",
    "certuspronx_evn",
    "certuspronx_versa_evn",
    "cmod_s7",
    "cmoda7_15t",
    "cmoda7_35t",
    "colorlight",
    "colorlight-i5",
    "colorlight-i9",
    "colorlight-i9+",
    "crosslinknx_evn",
    "cyc1000",
    "cyc5000",
    "de0",
    "de0nano",
    "de0nanoSoc",
    "de10lite",
    "de10nano",
    "de1Soc",
    "deca",
    "dragonL",
    "ecp5_evn",
    "ecpix5",
    "ecpix5_r03",
    "efinix_jtag_ft2232",
    "fireant",
    "fomu",
    "gatemate_evb_jtag",
    "gatemate_evb_spi",
    "gatemate_pgm_spi",
    "genesys2",
    "gr740-mini",
    "honeycomb",
    "hseda-xc6slx16",
    "ice40_generic",
    "ice40_generic",
    "ice40_generic",
    "ice40_generic",
    "ice40_generic",
    "ice40_generic",
    "ice40_generic",
    "icebreaker-bitsy",
    "kc705",
    "kcu105",
    "kcu116",
    "licheeTang",
    "lilygo-t-fpga",
    "litex-acorn-baseboard-mini",
    "machXO2EVN",
    "machXO3EVN",
    "machXO3SK",
    "mimas_a7",
    "mini_itx",
    "nexysVideo",
    "nexys_a7_100",
    "nexys_a7_50",
    "olimex_gatemateevb",
    "orangeCrab",
    "orbtrace_dfu",
    "papilio_one",
    "pipistrello",
    "pynq_z1",
    "pynq_z2",
    "qmtechCyclone10",
    "qmtechCycloneIV",
    "qmtechCycloneV",
    "qmtechCycloneV_5ce523",
    "qmtechKintex7",
    "redpitaya14",
    "runber",
    "runber",
    "spartanEdgeAccelBoard",
    "stlv7325",
    "tangmega138k",
    "tangnano",
    "tangnano1k",
    "tangnano20k",
    "tangnano4k",
    "tangnano9k",
    "tangprimer20k",
    "tangprimer25k",
    "te0712_8",
    "tec0117",
    "tec0330",
    "trion_t120_bga576",
    "trion_t120_bga576_jtag",
    "trion_t20_bga256_jtag",
    "trion_ti60_f225",
    "trion_ti60_f225_jtag",
    "ulx3s",
    "ulx3s_dfu",
    "usrpx300",
    "usrpx310",
    "vc709",
    "vcu108",
    "vcu118",
    "vcu128",
    "vcu1525",
    "vec_v6",
    "xem8320",
    "xmf3",
    "xtrx",
    "xyloni_spi",
    "zc702",
    "zc706",
    "zcu102",
    "zcu106",
    "zedboard",
    "zybo_z7_10",
    "zybo_z7_20",
]
CABLES = [
    "anlogicCable",
    "arm-usb-ocd-h",
    "bus_blaster",
    "bus_blaster_b",
    "ch347",
    "ch347_jtag",
    "ch552_jtag",
    "cmsisdap",
    "dfu",
    "digilent",
    "digilent_hs2",
    "digilent_hs3",
    "diglent_b",
    "dirtyJtag",
    "ecpix5-debug",
    "efinix_jtag_ft2232",
    "efinix_jtag_ft4232",
    "efinix_spi_ft2232",
    "efinix_spi_ft4232",
    "ft2232",
    "ft2232_b",
    "ft231X",
    "ft232",
    "ft232RL",
    "ft4232",
    "ft4232hp",
    "ft4232hp_b",
    "gatemate_evb_jtag",
    "gatemate_evb_spi",
    "gatemate_pgm",
    "gwu2x",
    "jetson-nano-gpio",
    "jlink",
    "jtag-smt2-nc",
    "libgpiod",
    "lpc-link2",
    "numato",
    "orbtrace",
    "papilio",
    "remote-bitgang",
    "steppenprobe",
    "tigard",
    "usb-blaster",
    "usb-blasterII",
    "xvc-client",
    "xvc-server",
]
FPGAS = [
    "xc3s500evq100",
    "xc6slx9tqg144",
    "xc6slx9csg324",
    "xc6slx16ftg256",
    "xc6slx16csg324",
    "xc6slx25csg324",
    "xc6slx45csg324",
    "xc6slx100fgg484",
    "xc6slx25tcsg324",
    "xc6slx45tfgg484",
    "xc6slx150tfgg484",
    "xc6slx150tcsg484",
    "xc6vlx130tff784",
    "xc7a15tcpg236",
    "xc7a25tcpg238",
    "xc7a25tcsg325",
    "xc7a35tcpg236",
    "xc7a35tcsg324",
    "xc7a35tftg256",
    "xc7a35tfgg484",
    "xc7a50tcsg324",
    "xc7a50tfgg484",
    "xc7a50tcpg236",
    "xc7a75tfgg484",
    "xc7a100tcsg324",
    "xc7a100tfgg484",
    "xc7a100tfgg676",
    "xc7a200tsbg484",
    "xc7a200tfbg484",
    "xc7a200tfbg676",
    "xc7s6ftgb196",
    "xc7s25csga225",
    "xc7s25csga324",
    "xc7s50csga324",
    "xc7k70tfbg484",
    "xc7k70tfbg676",
    "xc7k160tffg676",
    "xc7k325tffg676",
    "xc7k325tffg900",
    "xc7k420tffg901",
    "xcku3p-ffva676",
    "xc7vx330tffg1157",
    "xcku040-ffva1156",
    "xcku060-ffva1156",
    "xcku5p-ffvb676",
    "xcvu9p-flga2104",
    "xcvu37p-fsvh2892",
]

BOARDS.sort(key=lambda s: s.lower())
CABLES.sort(key=lambda s: s.lower())
FPGAS.sort(key=lambda s: s.lower())