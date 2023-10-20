class PascalCase {

	struct PascalCase {}

	interface IPascalCase {}

	//  i know about some conventions but PascalCase in public
	// fields, props, ev, methods is only for setget, coz screw it
	public int camelCasePublic;

	private int _camelCasePrivate;
	protected int _camelCaseProtected;

	//  static follows same rule as normal, except private
	// privates goes as s_
	public static int camelCaseStaticPublic;

	private static int s_camelCase;

	// thread statics changes s -> t
	private static int t_camelCase;

	// consts follow the same rules as usual varuables
	private readonly int _camelCaseReadonly;
	public const int camelCaseConst;

	// naming order is:
	public static abstract const int constValue;
	// or:
	private static virtual readonly int s_readonlyValue;
	// visibility, isStatic, anything else, isConst, type, name
	// aka: 
	// public/private/protected static abstract/virtual delegate override readonly/const int varName;

	// methods usually follow the main rules for particular language
	// so for c# it's PascalCase, for Java is camelCase, for c it's snake_case
	void method_case(){} // ???
	void MethodCase(){} // ???
	void methodCase(){} // ???

	// usually enum follows language convention
	// but might be some exceptions
	// for c#
	enum PascalCase {
		PascalCaseType1,
		PascalCaseType2
	}
	// for Dlang: 
	enum PascalCase {
		camelCaseType1,
		camelCaseType2
	}

	// for keywords add _ in end
	int int_;
	bool bool_;

	// acronyms 
	// follow first letter
	string asciiString;
	string UTFString;

	// brackets
	// ONE TRUE BRACE STYLE
	// Aka
	void function() {

		// with one exception of if else if
		// goes like this
		if (bool_) {

		} else
		if (int_ == 0) {

		}

	}

	// comments goes like this
	// one space apart from slashes

	/* or same way with multiline
	 * like this
	 */

	/* tho this
	   is also allowed
	   as long as 
	   it's all on same level
	 */

	// BUT documentation follows:

	/// Triple for single likes

	/**
	 * Double for multi
	 * doc
	 */
}

