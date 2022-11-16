Name:		texlive-scontents
Version:	62902
Release:	1
Summary:	Stores LaTeX contents in memory or files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scontents
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scontents.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scontents.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scontents.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package stores valid LaTeX code in memory (sequences)
using the l3seq module of expl3. The stored content (including
verbatim) can be used as many times as desired in the document,
additionally can be written to external files if desired.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/scontents
%{_texmfdistdir}/tex/latex/scontents
%{_texmfdistdir}/tex/generic/scontents
%{_texmfdistdir}/tex/context/third/scontents
%doc %{_texmfdistdir}/doc/latex/scontents

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
