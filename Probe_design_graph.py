
from Bio.Seq import Seq
from dna_features_viewer import GraphicFeature, GraphicRecord
#import sys
import os

file = input("Enter the Sequence File:" )
name = input("Enter the Name of the Sequence: ")
initiator = input("Enter the Initiator: ")


def probe_graph(file_name, path):
    #file_name = "results_riftl_test.txt"
    #file_name = sys.argv[1]
    f = open(file_name, "r")
    probes = []
    for line in f:
        print(line)
        line_info = line.split(':')
        #print(line)
        #print(line_info)
        if (line_info[0] == "Sequence"):
            sequence = line_info[1]
        elif(line_info[0] == "Initiator"):
            initiator1 = line_info[1].upper()
            initiator2 = line_info[2].upper()
        elif(line_info[0] == "Probes"):
            probes.append(line_info[1].upper())
            probes.append(line_info[3].upper())
            probes.append(line_info[2])
            probes.append(line_info[4])
        elif(line_info[0] == "Name"):
            name = line_info[1].rstrip()
    file_write = path + "/" +  name + "_Probe_Set" ".txt"
    w = open(file_write, "w+")
    """print(sequence)
    print(initiator1)
    print(initiator2)
    print(probe1)
    print(probe2)
    print(start)"""
    x = 1
    print(probes)
    print(name)
    for a in range(0, len(probes), 4):
        gstart = 28
        gend = 3
        probe1 = probes[a]
        probe2 = probes[a + 1]
        probe1 = Seq(probe1)
        probe1 = probe1.complement()
        probe2 = Seq(probe2)
        probe2 = probe2.complement()
        probe1 = str(probe1)
        probe2 = str(probe2)
        start = probes[a + 2]
        end = probes[a + 3]
        start = int(start)
        start -= 4
        if start <= 0:
            gend = 0 - start - 1
            gstart = gend + 25
            start = 0
        end = int(end)
        subseq = sequence[start:end]
        subseq = subseq.upper()
        record = GraphicRecord(sequence = subseq, features = [GraphicFeature(start = gstart, 
        end = gend, strand = +1, color = '#ffcccc', label = probe1), GraphicFeature(start = gstart + 28,
        end = gstart + 2, strand = +1, color = '#ccccff', label = probe2), GraphicFeature(start =gstart,
        end = gstart, strand = -1, color = 'm', label = "space"), GraphicFeature(start =gstart + 1,
        end = gstart + 1, strand = -1, color = 'm', label = "space"), GraphicFeature(start = gstart, end = (gstart -
        len(initiator1)), strand = -1, color = 'y', label = initiator1), GraphicFeature(start = gstart + 2,
        end = (gstart + 2 + len(initiator1)), strand = +1, color = 'y', label = initiator2)])
        ax, _ = record.plot(figure_width = 10)
        record.plot_sequence(ax)
        total1 = initiator1 + "TT" + probe1[::-1]
        total2 = probe2[::-1] + "TT" + initiator2
        w.write("PROBE SET" + str(x) + "\n")
        w.write("Probe1:" + total1 + "\n")
        w.write("Probe2:" + total2 + "\n")
        #print(total2)
        tosave =  path + "/" + name + "Plots for Probes" + str(x)
        x += 1
        ax.figure.savefig(tosave, bbox_inches = 'tight')
        #break
    w.close()
    
def design_probe(file_name, name, initiator, path):
    #file_name = "H:\Alex\probe_visual\\riftl.txt"
    f = open(file_name, "r")
    for line in f:
        print(line)
        sequence = line
        
    probe1 = ''
    probe2 = ''
    temp = ''
    first = True
    middle1 = False
    middle2 = False
    probes = []
    x = 0
    while x < len(sequence):
        temp = ''
        print(x)
        if x + 25 >=len(sequence):
            print("breakout")
            break
        for y in range(x, len(sequence)):
            #if y + 25 >= len(sequence):
                #break
            char = sequence[y]
            #print(char)
            length = len(temp)
            #print(length)
            #print(temp)
            temp += char
            print(temp)
            #print(first)
            if middle1:
                #print("INTHEMIDDLE")
                middle2 = True
                middle1 = False
                temp = ''
                #continue
            elif middle2:
                #print("SECONDMIDDLE")
                middle2 = False
                temp = ''
                #continue
            elif char.isupper() and first == True:
                temp = ''
                break
            elif char.isupper() and first == False:
                probe1 = ''
                temp = ''
                first = True
                break
            elif length == 24 and first == True:
                first = False
                probe1 = temp
                temp = ''
                middle1 = True
                num = y -23
                probe1 = probe1 + ":" + str(num)
                print(y)
                #x = y
                #print(temp)
            elif length == 24 and first == False:
                first = True
                probe2 = temp
                temp = ''
                #print(y)
                print("GOT ONE?")
                probe2 = probe2 + ":" + str(y)
                probes.append(probe1)
                probes.append(probe2)
                probe1 = ''
                probe2 = ''
                #print(x)
                print(y)
                middle1 = True
                x = y
                break
        #print(probe1)
        #print(probe2)
        x += 1
    print(probes)
    q = 1
    write_file = path + "/results_" + name + "_test.txt"
    w = open(write_file, "w")
    w.write("Name:" + name + "\n")
    w.write("Sequence:" + sequence + "\n")
    i1 = initiator[:int(len(initiator)/2)]
    i2 = initiator[int(len(initiator)/2):]
    w.write("Initiator:" + i1 + ":" + i2 + ":\n")
    for z in probes:
        if q == 1:
            w.write("Probes:" + z.upper() + ":")
            q = 2
        else:
            w.write(z.upper() + "\n")
            q = 1
    w.close()
    probe_graph(write_file, path)
    
path = 'H:/Alex/probe_visual/' + name + 'probe_design'
os.mkdir(path)
design_probe(file, name, initiator, path)
