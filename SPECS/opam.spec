%ifarch %{ocaml_native_compiler}
%global native_compiler 1
%else
%global native_compiler 0
%endif

Name:           opam
Version:        1.2.0
Release:        1%{?dist}
Summary:        A source-based package manager for OCaml
License:        LGPLv3 with exceptions
URL:            http://opam.ocaml.org
Source0:        https://github.com/ocaml/opam/archive/1.2.0/opam-1.2.0.tar.gz
Patch0:         opam-lib-install-fix
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-jsonm-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-dose3-devel
BuildRequires:  ocaml-uutf-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  zlib-devel
BuildRequires:  chrpath

%description
OPAM is a source-based package manager for OCaml. It supports multiple
simultaneous compiler installations, flexible package constraints, and
a Git-friendly development workflow.

%package        -n ocaml-opam-lib
Summary:	An OCaml Library to manipulate OPAM packages

%description -n ocaml-opam-lib
OPAM is a source-based package manager for OCaml. It supports multiple
simultaneous compiler installations, flexible package constraints, and
a Git-friendly development workflow.

This package contains the runtime components of the core OPAM
libraries for use in other OCaml programs.

%package        -n ocaml-opam-lib-devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    -n ocaml-opam-lib-devel
OPAM is a source-based package manager for OCaml. It supports multiple
simultaneous compiler installations, flexible package constraints, and
a Git-friendly development workflow.

This package contains the development signatures and libraries for
developing application using the core OPAM libraries in other OCaml
programs.


%prep
%setup -q
%patch0 -p1

%build
./configure --prefix /usr --libdir %{_libdir}
make
make man

%check

%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
export DESTDIR=$RPM_BUILD_ROOT
make -e install 
make LIBINSTALL_DIR=$RPM_BUILD_ROOT%{_libdir}/ocaml libinstall
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/opam $RPM_BUILD_ROOT%{_bindir}/opam-admin $RPM_BUILD_ROOT%{_bindir}/opam-installer
rm $RPM_BUILD_ROOT%{_bindir}/opam-admin.top

%files
%doc README.md LICENSE CONTRIBUTING.md AUTHORS CHANGES
%{_bindir}/opam
%{_bindir}/opam-admin
%{_bindir}/opam-installer
%{_mandir}/man1/opam*

%files -n ocaml-opam-lib
%{_libdir}/ocaml/opam-lib
%if %{native_compiler}
%exclude %{_libdir}/ocaml/opam-lib/*.a
%exclude %{_libdir}/ocaml/opam-lib/*.cmxa
%exclude %{_libdir}/ocaml/opam-lib/*.cmx
%endif
%exclude %{_libdir}/ocaml/opam-lib/*.mli

%files -n ocaml-opam-lib-devel
%if %{native_compiler}
%{_libdir}/ocaml/opam-lib/*.a
%{_libdir}/ocaml/opam-lib/*.cmx
%{_libdir}/ocaml/opam-lib/*.cmxa
%endif
%{_libdir}/ocaml/opam-lib/*.mli


%changelog 
* Wed Dec 17 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.0-1
- Initial package

