%global tl_name scontents
%global tl_revision 79225

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.7
Release:	%{tl_revision}.1
Summary:	Stores LaTeX contents in memory or files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scontents
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scontents.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scontents.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scontents.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package stores valid LaTeX code in memory (sequences) using the
l3seq module of expl3. The stored content (including verbatim) can be
used as many times as desired in the document, additionally can be
written to external files if desired.

