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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX Beamer theme designed for the Department of Economics at
Bilkent University. It provides a clean, professional presentation style
with department-specific colors, custom title pages, and consistent
slide formatting for lectures, seminars, and research talks.

