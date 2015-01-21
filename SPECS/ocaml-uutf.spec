%ifarch %{ocaml_native_compiler}
%global native_compiler 1
%else
%global native_compiler 0
%endif

Name:           ocaml-uutf
Version:        0.9.3
Release:        4%{?dist}
Summary:        Non-blocking streaming codec for UTF-8, UTF-16, UTF-16LE and UTF-16BE
License:        BSD
URL:            http://erratique.ch/software/uutf
Source0:        https://github.com/dbuenzli/uutf/archive/v%{version}/uutf-%{version}.tar.gz
Patch0:         uutf-enable-debug
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
Uutf is an non-blocking streaming Unicode codec for OCaml to decode and
encode the UTF-8, UTF-16, UTF-16LE and UTF-16BE encoding schemes. It can
efficiently work character by character without blocking on IO. Decoders
perform character position tracking and support newline normalization.

Functions are also provided to fold over the characters of UTF encoded
OCaml string values and to directly encode characters in OCaml Buffer.t
values.

Uutf is made of a single, independent, module and distributed under the
BSD license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n uutf-%{version}
%patch0 -p1

%build
./pkg/pkg-git
./pkg/build true

%install
mkdir -p %{buildroot}%{_libdir}/ocaml/uutf
DEST=%{buildroot}/%{_libdir}/ocaml/uutf
cp _build/src/*.{cmi,cma,mli} _build/pkg/META ${DEST}
%ifarch %{ocaml_native_compiler}
cp _build/src/*.{a,cmx,cmxa} ${DEST}
%endif
%ifarch %{ocaml_natdynlink}
cp _build/src/*.cmxs ${DEST}
%endif

%files
%doc CHANGES.md
%doc README.md
%{_libdir}/ocaml/uutf
%exclude %{_libdir}/ocaml/uutf/*.mli
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/uutf/*.a
%exclude %{_libdir}/ocaml/uutf/*.cmxa
%exclude %{_libdir}/ocaml/uutf/*.cmx
%endif

%files devel
%{_libdir}/ocaml/uutf/uutf.mli
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/uutf/uutf.a
%{_libdir}/ocaml/uutf/uutf.cmxa
%{_libdir}/ocaml/uutf/uutf.cmx
%endif

%changelog
* Fri Jan 16 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.3-4
- Minor fixes for Fedora

* Mon May 19 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-3
- Switch to GitHub mirror

* Fri Oct 18 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-2
- 'Ported' from xen-dist-ocaml to xenserver-core

* Fri Oct 11 2013 Jon Ludlam <jonathan.ludlam@eu.citrix.com> - 0.9.3-1
- Initial RPM release 