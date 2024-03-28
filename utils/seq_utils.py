#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc_ham_dist(seq1, seq2, to_ref=True):
    """
    Calculate Hamming distance between 2 sequences of varying lengths, trim if larger
    Input: 2 sequences, flag to use the first sequence as reference
    Returns: Hamming distance
    """
    d = sum(s1 != s2 for (s1, s2) in zip(seq1, seq2))
    if to_ref: d = d/len(seq1)
    return d
    
def calc_intergenic_dist(pos1, pos2, contig_len=None):
    """
    Calculate intergenic distance between two genes on the same contig, also 
    takes strandedness into account
    Input: positions of 2 genes (as intervals), circular flag (default: True)
    and contig length (necessary only for circular contigs)
    Returns the intergenic distance - or None if the genes are on different strands
    ref: Mihelčić, M., Šmuc, T. & Supek, F. Patterns of diverse gene functions 
    in genomic neighborhoods predict gene function and phenotype. 
    Sci Rep 9, 19537 (2019). https://doi.org/10.1038/s41598-019-55984-0
    """
    if pos1[-1] != pos2[-1]:
        return None
    if pos1[0] > pos2[1]:
        corpos1 = pos2
        corpos2 = pos1
    elif pos2[0] > pos1[1]:
        corpos1 = pos1
        corpos2 = pos2
    else:
        return 0
    if contig_len:
        d = min(abs(corpos2[0] - corpos1[1]), abs(corpos2[1] - contig_len - corpos1[0]))
    else:
        d = abs(corpos2[0] - corpos1[1])

    return d
