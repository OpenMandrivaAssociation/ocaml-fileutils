%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml library for common file and filename operations
Name:		ocaml-fileutils
Version:	0.4.5
Release:	1
License:	LGPLv2+
Group:		Development/Other
Url:		http://ocaml-fileutils.forge.ocamlcore.org/
Source0:	http://forge.ocamlcore.org/frs/download.php/1194/ocaml-fileutils-%{version}.tar.gz
BuildRequires:	camlp4
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ounit

%description
This library is intended to provide a basic interface to the most
common file and filename operations.  It provides several different
filename functions: reduce, make_absolute, make_relative...  It also
enables you to manipulate real files: cp, mv, rm, touch...

It is separated into two modules: SysUtil and SysPath.  The first one
manipulates real files, the second one is made for manipulating
abstract filenames.

%files
%doc README.txt
%dir %{_libdir}/ocaml/fileutils
%{_libdir}/ocaml/fileutils/*.cmi
%{_libdir}/ocaml/fileutils/*.cma
%{_libdir}/ocaml/fileutils/*.cmxs
%{_libdir}/ocaml/fileutils/META

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc COPYING.txt AUTHORS.txt CHANGELOG.txt README.txt TODO.txt
%{_libdir}/ocaml/fileutils/*.a
%{_libdir}/ocaml/fileutils/*.cmx
%{_libdir}/ocaml/fileutils/*.cmxa
%{_libdir}/ocaml/fileutils/*.ml
%{_libdir}/ocaml/fileutils/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q

%build
ocaml setup.ml -configure
ocaml setup.ml -build

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install

%check
ocaml setup.ml -test
