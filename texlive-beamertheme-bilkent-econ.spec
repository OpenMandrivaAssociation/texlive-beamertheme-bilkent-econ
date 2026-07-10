%global tl_name beamertheme-bilkent-econ
%global tl_revision 76561

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	LaTeX Beamer theme for the Department of Economics at Bilkent University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-bilkent-econ
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-bilkent-econ.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-bilkent-econ.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX Beamer theme designed for the Department of Economics at
Bilkent University. It provides a clean, professional presentation style
with department-specific colors, custom title pages, and consistent
slide formatting for lectures, seminars, and research talks.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-bilkent-econ
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-bilkent-econ
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-bilkent-econ/BilkentEconTemplateGuide.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-bilkent-econ/BilkentEconTemplateGuide.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-bilkent-econ/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-bilkent-econ/README
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-bilkent-econ/beamertheme-bilkent-econ-example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-bilkent-econ/beamertheme-bilkent-econ-example.tex
%{_datadir}/texmf-dist/tex/latex/beamertheme-bilkent-econ/beamertheme-bilkent-econ.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-bilkent-econ/bilkent_logo.png
